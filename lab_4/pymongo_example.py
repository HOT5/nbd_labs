from pymongo import MongoClient


def fill_database_with_books(mongo_client: MongoClient):
    ikol5DB = mongo_client.ikol5DB
    books_collection = ikol5DB.collection_books
    pymongo_book = {
        'Title': 'Learn PyMongo connector',
        'Content': 'This book will teach you how to connect to MongoDB via PyMongo',
        'Author': 'PyMongo'
    }

    result = books_collection.insert_one(pymongo_book)
    print(f'{pymongo_book.get("Title")} was added to book collection with id {result.inserted_id}')

    java8_book = {
        'Title': 'Java 8 new features',
        'Content': 'This book will teach you new features of Java 8',
        'Author': 'Java'
    }

    aws_ec2_book = {
        'Title': 'Learn AWS Elastic Compute Cloud',
        'Content': 'This book will teach how manage AWS ec2 instances',
        'Author': 'AWS'
    }

    aws_s3_book = {
        'Title': 'Learn AWS Simple Storage Service',
        'Content': 'This book will teach how manage AWS Simple Storage Service',
        'Author': 'AWS'
    }

    books = [java8_book, aws_ec2_book, aws_s3_book]

    result = books_collection.insert_many(books)

    print(f'{len(books)} books was added to book collection with ids {result.inserted_ids}')


def find_one_book_by_author(mongo_client: MongoClient, author: str):
    return mongo_client.ikol5DB.collection_books.find_one({'Author': author})


def find_books_by_author(mongo_client: MongoClient, author: str):
    return mongo_client.ikol5DB.collection_books.find({'Author': author})


if __name__ == '__main__':
    mongo_client = MongoClient('localhost', 27017)
    fill_database_with_books(mongo_client)
    book = find_one_book_by_author(mongo_client, 'Java')
    print(book)
    books = find_books_by_author(mongo_client, 'AWS')
    for book in books:
        print(book)
