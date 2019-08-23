import time
import requests
import json
product_file = open('product.csv','a')
Header = 'Name,Title,Organaization,Visit data\n'
product_file.write(Header) #writing header of csv file

reading = open('s_list.csv','r') #reading slug list file
l = reading.read().split('\n')



def requesting(i):
  data = requests.get('https://www.politico.com/interactives/databases/trump-white-house-visitor-logs-and-records/api/visitor/{0}.json'.format(i))
  print('status code received {0}'.format(data.status_code))
  if data.status_code != 200:
    return 404
  else:
    js_data = json.loads(data.text)
    return js_data


def process(data):
  if data['middle_initial'] is not None:
    full_name = '{0} {1} {2}'.format(data['first_name'],data['middle_initial'],data['last_name'])
  else:
    full_name = '{0} {1}'.format(data['first_name'],data['last_name'])
  title = data['title']
  org = data['organization']
  org_name = ''
  if org is not None:
    for  i,j in org.items():
      org_name += '{0}'.format(j)
  else:
    pass
  visit = data['visits']
  visit_date_list = []
  for i in visit:
    visit_date_list.append(i.get('date'))
  Full_data = ' {0},{1},{2},{3}\n\n'.format(full_name,title,org_name,visit_date_list)
  product_file.write(Full_data)
  return "Done"

print('Your job staring now')
counter = 1
for i in l[1:]:
  print('working {0} no idex'.format(counter))
  recieved = requesting(i)
  if recieved != 404:

    process(recieved)
  else:
    print('some problem with index number --{0} name=={1}'.format(l.index(i),i))
  time.sleep(3)
  counter +=1
product_file.close()