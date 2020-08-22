import xlrd as xlrd
import openpyxl as xl
file_name="/Users/emily/Downloads/巨量資料與金融科技實務期末報告檔案-copy/1Q_Chg._Alpha_Monthly (1).xlsx"

data = xlrd.open_workbook(file_name)
sheet_alpha=data.sheet_by_name("合併月報酬資料") #alpha
time = sheet_alpha.row_values(0)
company = sheet_alpha.col_values(0)
te=[]
rank = []
sort_n=[]
for a in range(len(time)-2):
    te.append(a)

for a in range(len(company)-1):
    sort_n.append(a)

for a in range(len(company)-1):
    rank.append(a)

for a in range(2,len(time)):
    te[a-2] = sheet_alpha.col_values(a)


newfile="/Users/emily/Desktop/merge_al.xlsx"
wother = xl.load_workbook(newfile)
we = wother.worksheets[3] # 2是alpha rank

for a in range(len(time)-2):
     for i in range(1,len(te[a])):
         rank[i-1]=te[a][i]
          
     rank.sort(reverse=True)
    
     for j in range(len(rank)):
        for k in range(1,len(te[a])):
            if rank[j] == te[a][k]:
                 sort_n[k-1] = j+1
     print(sort_n)
     we.append(sort_n)

wother.save('/Users/emily/Desktop/merge_al.xlsx')

# sort_n=[]

# for a in range(len(rank)):
#     sort_n.append(a)

# for i in range(len(rank)):
#     for j in range(1,len(te)):
#         if rank[i]==te[j]:
#             sort_n[j-1]=i+1





