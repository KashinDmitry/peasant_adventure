from __future__ import print_function
from googleapiclient.discovery import build
from google.oauth2 import service_account
from classes import Player


SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
SAMPLE_SPREADSHEET_ID = '1-yN8OxNsgkXNNV-bgshAR2Oi4254oJGO71_mVPlOjUQ'
service = build('sheets', 'v4', credentials=creds)


def get_score_results_from_table(range):
    # range example "Scores!A2:B11"
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range).execute()
    values = result.get('values', [])
    return values


def insert_player_result_to_table(player):
    range_ = 'Scores!A1:B1'
    value_input_option = 'RAW'
    insert_data_option = 'INSERT_ROWS'
    value_range_body = {
        "values": [
            [player.name, Player.global_game_score]
        ]
    }
    request = service.spreadsheets().values().append(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body).execute()


def sort_score_table():
    request_body = {
        'requests': [
            {
                'setBasicFilter': {
                    'filter': {
                        'range': {
                            'sheetId': 0,
                            'startRowIndex': 0,
                            'startColumnIndex': 0
                        },
                        'sortSpecs': [
                            {
                                'dimensionIndex': 1,
                                'sortOrder': 'DESCENDING'
                            }
                        ]
                    }
                }
            }
        ]
    }
    response = service.spreadsheets().batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID, body=request_body).execute()


def delete_unused_scores():
    request_body_delete_rows = {
        'requests': [
            {
                'deleteDimension': {
                    'range': {
                        'sheetId': 0,
                        'dimension': 'ROWS',
                        'startIndex': 11,
                        'endIndex': 51
                    }
                }
            }
        ]
    }
    response = service.spreadsheets().batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID, body=request_body_delete_rows).execute()

