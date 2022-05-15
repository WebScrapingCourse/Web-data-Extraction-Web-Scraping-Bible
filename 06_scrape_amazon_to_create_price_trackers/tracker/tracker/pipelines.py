import gspread
from datetime import date
import smtplib

class TrackerPipeline:
    sender = "...@yahoo.com"
    sender_password = "..."
    receiver = "....@gmail.com"
    header = ["date", "name", "price", "site", "description", "price variation (compared to the max of last  7 days)"]
    def email_sender(self, name, price_variation):
        try:
            smtp = smtplib.SMTP_SSL('smtp.mail.yahoo.com')
            smtp.login(self.sender, self.sender_password)
            message = """
            From: From Python-price-tracker 
            Hello there. I bring some good news.
            On these days the price of the article {0} has been reduced by {1}%
            """.format(name, price_variation)
            smtp.sendmail(self.sender, self.receiver, message)
            smtp.close()
        except Exception as e:
            print(e)

    def gspread_wrapper(self, new_row):
        gc = gspread.service_account()
        wks = gc.open("python_tracker_sheet").sheet1  # Open the sheet1 from a spreadsheet
        if not wks.get_all_values(): wks.update("A1",[self.header]) and wks.append_rows([["_"]]*7*2, table_range="A6")
        # Delete the older row and add the new row
        wks.delete_rows(6)
        wks.append_row(new_row)

        # Update the top-rows
        _dict={"amazon.co.uk":"A2", "groupon.co.uk":"A3"}
        min_price = max([float(row[2]) for row in wks.get_all_values()[4:] if new_row[1]==row[1]] or [0])
        price_variation = float(new_row[2])-min_price
        new_row.append(str(price_variation)+"%")
        wks.update(_dict[new_row[3]], [new_row])

        # Send email notification
        if int(price_variation) < 0:
            self.email_sender(new_row[1],str(price_variation))

    def process_item(self, item, spider):
        row = [date.today().isoformat(),item["name"], item["price"], item["site"], item["description"]]
        self.gspread_wrapper(row)
