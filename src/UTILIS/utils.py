import pymongo
import sys
import os
from src.exception import CustomException
from src.logger import logging

class FetchQuestioninfo:
    def __init__(self, connection_string: str, db_name: str):
        try:# Initialize MongoDB connection
            self.client = pymongo.MongoClient(connection_string)
            logging.info("Connecting to Database")
            self.db = self.client['org-db']
            logging.info("Connected to Database")

            logging.info("Connecting to Collection")
            self.user_collection = self.db['users']
            self.question_collection = self.db['questions']
            logging.info("Connected to Collection")

        except Exception as e:
            raise CustomException(e,sys)


    def get_latest_question_info(self):
        
        try:
            # Get the most recent question
            logging.info("Searching question id in question Collection")
            latest_doc = self.question_collection.find_one(sort=[('createdAt', -1)])
        
            if not latest_doc:
                return {
                    "message": "No questions found.",
                    "postedBy": None,
                    "photoUrl": None
                }

            # Extract postedBy and image/text info
            user_id = latest_doc.get('postedBy')
            image_url = latest_doc.get('photoUrl')
            question_text = latest_doc.get('text')
        
            # Prioritize image, fallback to text
            content = image_url if image_url else question_text
            logging.info("Seach Completed in Collection")

            return {
                "postedBy": str(user_id),
                #"photoUrl": image_url,
                "content": content
            }
        except Exception as e:
            raise CustomException(e,sys)
