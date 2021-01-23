import os, random, time, random, spider
import urllib.request as u_request

def save(new_pic):
    count = 0
    for each in new_pic:
        try:
            req = u_request.Request(each, headers = spider.headers)
            response = u_request.urlopen(req)
            cat_image = response.read()
            filename = each.split('/')[-1]
            with open(filename,'wb') as f:
                f.write(cat_image)
            print(each)
        except OSError as error:
            print(error)
            continue
        except ValueError as error:
            print(error)
            continue
        sleep_time = round(random.uniform(0,0.05),5)
        time.sleep(sleep_time)

        count += 1
        print("successful: " + str(count) + '/' + str(len(new_pic)))