init -20 python:

    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

define scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
define creds = ServiceAccountCredentials.from_json_keyfile_name("C:/Users/it/the-mosaic-project-test-e32bf4fff7a5.json", scope)

default client = gspread.authorize(creds)
default sheet = client.open("The Mosaic Project - Test spreadsheet").sheet1

init -15 python:

    def updateData():
        return store.sheet.get_all_records()