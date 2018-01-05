'''
    
    Author: Vignesh Natarajan (www.vikilabs.in)
    
'''

import csv

foursquare_csv = "CSV PATH"

rest_list = []
rd_cnt = 0

rest_id = {}    #0
contact = {}    #1
locality = {}   #2
url = {}        #3
price = {}      #4
mon = {}        #5
tue = {}        #6
wed = {}        #7
thu = {}        #8
fri = {}        #9
sat = {}        #10
sun = {}        #11





def get_records_from_foursquare_csv():
    global rd_cnt

    with open(foursquare_csv, "r") as file:
        reader = csv.reader(file, delimiter=",")
        ctr = 0
        for row in reader:

            try:
                rest_id[ctr] = row[0]
            except:
                rest_id[ctr] = ""

            try:
                contact[ctr] = row[1]
            except:
                contact[ctr] = ""

            try:
                locality[ctr] = row[2]
            except:
                locality[ctr] = ""
            try:
                url[ctr] = row[3]
            except:
                url[ctr] = ""

            try:
                price[ctr] = row[4]
            except:
                price[ctr] = ""

            try:
                mon[ctr] = row[5]
            except:
                mon[ctr] = ""

            try:
                tue[ctr] = row[6]
            except:
                tue[ctr] = ""

            try:
                wed[ctr] = row[7]
            except:
                wed[ctr] = ""

            try:
                thu[ctr] = row[8]
            except:
                thu[ctr] = ""

            try:
                fri[ctr] = row[9]
            except:
                fri[ctr] = ""

            try:
                sat[ctr] = row[10]
            except:
                sat[ctr] = ""


            try:
                sun[ctr] = row[11]
            except:
                sun[ctr] = ""

            ''' 
            print ctr, "[ rest_id : "+ rest_id[ctr] +" ] ",
            print "[ contact : " + contact[ctr] + " ] ",
            print "[ locality : " + locality[ctr] + " ] ",
            print "[ url : " + url[ctr] + " ] ",
            print "[ price : " + price[ctr] + " ] ",
            print "[ mon : " +mon[ctr] + " ] ",
            print "[ tue : " +tue[ctr] + " ] ",
            print "[ wed : " +wed[ctr] + " ] ",
            print "[ thu : " +thu[ctr] + " ] ",
            print "[ fri : " +fri[ctr] + " ] ",
            print "[ sat : " +sat[ctr] + " ] ",
            print "[ sun : " +sun[ctr] + " ] "
            '''
            ctr = ctr + 1
            #rd_cnt += 1
            #if rd_cnt > 2:
            #   #print row[2]
            #  rest_list.append(row[2])



#Split string seperated by @ and put in a list
def get_open_timing_list(o_day):
    return o_day.split('@')

#get_records_from_foursquare_csv()

#end = len(mon)
#start = 1
#for i in range(start, end):
#    print i
#o_day = mon[19]
#print o_day

#o_list =  get_open_timing_list(o_day)

#print o_list
