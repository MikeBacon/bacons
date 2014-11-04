#1usr/bin/python

import pymongo

print "Hello World"


def main():
    client_col = pymongo.MongoClient()['test']['peyton_test']
    print client_col.find_one()


if __name__=='__main__':
    main()
