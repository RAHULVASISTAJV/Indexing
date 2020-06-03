import csv
import time
import pandas

def searchById():
  start = time.time()
  ID = str(input('Enter the id you want to search\n'))
  csv_file = csv.reader(open('cricket_data.csv', 'r', encoding='utf-8', errors='ignore'))
  flag = 0
  for row in csv_file:
    if ID == row[0]:
      print(row)
      flag = 0
      break
    else:
      flag = 1
  if flag == 1:
    print('Not Found')
  end = time.time()
  print('Process Completed in', end - start, 'seconds')


def searchByName():
  start1 = time.time()
  NAME = (input('Enter the Name You Want Search'))
  csv_file = csv.reader(open('cricket_data.csv', 'r', encoding='utf-8', errors='ignore'))
  flag1 = 0
  for row in csv_file:
    if NAME == row[1]:
      print(row)
      flag1 = 0
      break
    else:
      flag1 = 1
  if flag1 == 1:
    print('Not Found')
  end1 = time.time()
  print('Process Completed in', end1 - start1, 'seconds')


def searchByCOUNTRY():
  start2 = time.time()
  COUNTRY = (input('Enter the Country You Want Search'))
  csv_file = csv.reader(open('cricket_data.csv', 'r', encoding='utf-8', errors='ignore'))
  flag = 0
  for row in csv_file:
    if COUNTRY == row[2]:
      print(row)
      flag = 0
      break
    else:
      flag = 1
  if flag == 1:
    print('Not Found')
  end2 = time.time()
  print('Process Completed in', end2 - start2, 'seconds')


def searchByCurrentage():
  start3 = time.time()
  Currentage = (input('Enter the Age You Want Search'))
  csv_file = csv.reader(open('cricket_data.csv', 'r', encoding='utf-8', errors='ignore'))
  flag = 0
  for row in csv_file:
    if Currentage == row[4]:
      print(row)
      flag = 0
      break
    else:
      flag = 1
  if flag == 1:
    print('Not Found')
  end3 = time.time()
  print('Process Completed in', end3 - start3, 'seconds')


def searchByBattingstyle():
  start4 = time.time()
  Battingstyle = (input('Enter the Batting style You Want Search'))
  csv_file = csv.reader(open('cricket_data.csv', 'r', encoding='utf-8', errors='ignore'))
  flag = 0
  for row in csv_file:
    if Battingstyle == row[5]:
      print(row)
      flag = 0
      break
    else:
      flag = 1
  if flag == 1:
    print('Not Found')
  end4 = time.time()
  print('Process Completed in', end4 - start4, 'seconds')


def searchByBowlingstyle():
  start5 = time.time()
  Bowlingstyle = (input('Enter the Bowling style You Want Search'))
  csv_file = csv.reader(open('cricket_data.csv', 'r', encoding='utf-8', errors='ignore'))
  flag = 0
  for row in csv_file:
    if Bowlingstyle == row[6]:
      print(row)
      flag = 0
    else:
      flag = 1
  if flag == 1:
    print('Not Found')
  end5 = time.time()
  print('Process Completed in', end5 - start5, 'seconds')


def search():
  print('Enter\n 1. Search by Id\n 2. Search by Name\n 3. Search by Country\n 4. Search by Age'
        '\n 5. Search by Batting Style \n 6. Search by Bowling Style\n')

  src = int(input('Enter your choice\n'))
  if src == 1:
    searchById()
  elif src == 2:
    searchByName()
  elif src == 3:
    searchByCOUNTRY()
  elif src == 4:
    searchByCurrentage()
  elif src == 5:
    searchByBattingstyle()
  elif src == 6:
    searchByBowlingstyle()
  else:
    print('Invalid Choice')


def append():
  start6 = time.time()
  print('All the values are necessary')
  with open('cricket_data.csv', 'a+', newline='') as f:
    fieldnames = ['ID', 'NAME', 'COUNTRY', 'Current age', 'Full name', 'Batting style', 'Bowling style']
    tgwrite = csv.DictWriter(f, fieldnames=fieldnames)
    idinput = int(input('Enter the Id\n'))
    nameinput = input('Enter the Name\n')
    countryinput = input('Enter th country\n')
    fullnameinput = input('Enter the Full Name\n')
    ageinput = int(input('Enter the age\n'))
    batinput = input('Enter the batting style\n')
    ballinput = input('Enter the bowling style\n')
    add = {'ID': idinput, 'NAME': nameinput, 'COUNTRY': countryinput, 'Full name': fullnameinput,
           'Current age': ageinput, 'Batting style': batinput, 'Bowling style': ballinput}
    tgwrite.writerow(add)
    end6 = time.time()
    print('Values are appended')
    print('Process Completed in', end6 - start6, 'seconds')


def deletion():
  start11 = time.time()
  df = pandas.read_csv('cricket_data.csv', index_col=0)
  delid = int(input('Enter the Id you want to delete\n'))
  df.drop(delid, axis=0, inplace=True)
  df.to_csv('cricket_data.csv')
  print('Record Deleted Successfully')
  end11 = time.time()
  print('Process Completed in', end11 - start11, 'seconds')


def modify():
  start8 = time.time()
  df = pandas.read_csv('cricket_data.csv', index_col=False)
  Index = int(input("Enter your Index which is needed to be modified : "))
  print(df[df['ID'] == Index])
  Column = input("Enter your Column which is needed to be modified : ")
  print("OLD VALUE  " + df.loc[df['ID'] == Index, Column])
  Replace = input("Enter your data to be Replaced  : ")
  df.loc[df['ID'] == Index, Column] = Replace
  print("NEW VALUE   " + df.loc[df['ID'] == Index, Column])
  df.to_csv('cricket_data.csv', index=False)
  end8 = time.time()
  print('Process Completed in', end8 - start8, 'seconds')


def indexgen():
  start9 = time.time()
  with open("cricket_data.csv", "r", encoding='utf-8', errors='ignore') as pack:
    with open("cricket_data1.csv", "w", encoding='utf-8', errors='ignore') as index:
      count = 0
      for line in pack:
        stri = line[:8]
        index.write(stri)
        c = str(count)
        index.write(c + "\n")
        count = len(line) + count
      print('Index File Generated')
      end9 = time.time()
      print('Process Completed in', end9 - start9, 'seconds')


def searchByIndex():
  start10 = time.time()
  with open("cricket_data.csv", "r", encoding='utf-8', errors='ignore') as main1:
    with open("cricket_data1.csv", "r", encoding='utf-8', errors='ignore') as index1:
      lines = main1.readlines()
      search1 = input("Enter the id\n")
      start2 = time.time()
      for line1 in index1:
        if search1 in line1:
          print("The line is here in index file:" + line1)
          line1 = line1.split(",")
          loc = line1[1].split()
          locate = int(loc[0])
          x = main1.seek(locate)
          y = main1.readlines(locate)
          result = [ind for ind in y if search1 in ind]
          result1 = result[0].split(',')
          print(result1)
          end10 = time.time()
          print('Process Completed in', end10 - start10, 'seconds')
          break
      else:
          print('Not Found')

def main():
  while True:
    print('Enter \n 1.Search 2.Modify 3.Add 4.Delete 5.Generate an Index file 6.Search Using Index File 7.Exit\n')
    Choice = int(input('Enter your choice\n'))
    if Choice == 1:
      search()
    elif Choice == 2:
      modify()
    elif Choice == 3:
      append()
    elif Choice == 4:
      deletion()
    elif Choice == 5:
      indexgen()
    elif Choice == 6:
      searchByIndex()
    elif Choice == 7:
      print('Thanks')
      exit(0)
    else:
      print('Invalid Choice')


if __name__ == '__main__':
  main()
