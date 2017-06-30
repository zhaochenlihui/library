import requests
import re
import mysql.connector
def getHTMLText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print("error")
        return ""
def parsePage(html):
    try:
        reg=re.compile(r'<span class="briefcitTitle">\n<a href=.*?>(.*?)</a>\n</span>\n<br />\n<span class="briefcitDetail">\n(.*?)\n<br />\n<span class="briefcitDetail">\n(.*?)<br />\n<br />\n<span class="briefcitDetail">\n(.*?)<br />',re.S)
        ilt=reg.findall(html)
        return ilt
    except:
        print('error_re')
def parseLink(html):
    try:
        reg=re.compile(r'<a href=.*? target="_parent"><img src="(.*?)" .*?></a><td.*?>\n<.*?>\n<span class="briefcitTitle">\n<a href=.*?>(.*?)</a>\n</span>\n<br />\n<span class="briefcitDetail">\n(.*?)\n<br />\n<span class="briefcitDetail">\n(.*?)<br />\n<br />\n<span class="briefcitDetail">\n(.*?)<br />',re.S)
        link=reg.findall(html)
        return link
    except:
        print('error_link')
def printDatabase(ilt):
    for i in range(len(ilt)):
        try:
            conn=mysql.connector.connect(user='root',password='root',database='test')
            cursor=conn.cursor()
            cursor.execute('insert into book_without_link(book_name,book_author,book_publish,book_summary) values(%s,%s,%s,%s)',[ilt[i][0],ilt[i][1],ilt[i][2],ilt[i][3]])
            conn.commit()
            cursor.close()
            # print("成功插入第"+str(i)+"条数据")
        except:
            print('error_insert')
            continue
def printDatabase_link(link):
    for i in range(len(link)):
        try:
            conn=mysql.connector.connect(user='root',password='root',database='test')
            cursor=conn.cursor()
            cursor.execute('insert into book_with_link(book_name,book_author,book_publish,book_summary,book_link) values(%s,%s,%s,%s,%s)',[link[i][1],link[i][2],link[i][3],link[i][4],link[i][0]])
            conn.commit()
            cursor.close()
            # print("成功插入第"+str(i)+"条数据")
        except:
            print('error_insert_link')
            continue
def main():
    mdzz_1=['d0','d1','d2','d3','d4','d5', 'd6', 'd7', 'd8', 'd90', 'd91', 'd92', 'd93', 'd94', 'd95', 'd96', 'd97', 'd99', 'e', 'f0', 'f1', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f20', 'f21', 'f22', 'f23', 'f239', 'f24', 'f25', 'f27', 'f28', 'f29', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g0', 'g1', 'g2', 'g20', 'g21', 'g22', 'g23', 'g24', 'g25', 'g26', 'g27', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h0', 'h1', 'h2', 'h310.1', 'h310.4', 'h310.9', 'h311', 'h312', 'h313', 'h314', 'h315', 'h316', 'h317', 'h319', 'h32', 'h33', 'h34', 'h35', 'h36', 'h37', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9', 'i0', 'i1', 'i20', 'i21', 'i22', 'i23', 'i242', 'i246', 'i247.4','i247.5', 'i247.7', 'i247.8', 'i25', 'i26', 'i27', 'i28', 'i29', 'i3', 'i4', 'i5', 'i6', 'i7', 'j0', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'j8', 'j9', 'k0', 'k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7', 'k81', 'k82', 'k83', 'k85', 'k86', 'k87', 'k89', 'k9', 'n', 'o1-', 'o11', 'o12', 'o13', 'o14', 'o15', 'o17', 'o18', 'o19', 'o21', 'o22', 'o23', 'o24', 'o29', 'o3', 'o4', 'o4-', 'o41', 'o42', 'o43', 'o44', 'o46', 'o469','o47','o48','o5','o51','o52','o53','o55','o56','o57','o59','o6-','o61','o62','o63','o64','o65','o661','o7','p','q-','q1','q2','q3','q4','q5','q6','q7','q81','q91','q93','q94','q95','q96','q98','r-','r11','r12','r13','r14','r149','r15','r16','r17', 'r179','r18','r19','r2-','r21','r22','r24','r25','r26','r272','r273','r274','r275','r276','r277','r278','r28','r289','r9','r31','r32','r33','r34','r35','r36','r37','r38','r392','r394','r395','r44','r45','r47','r48','r49','r51','r52','r53','r54','r55','r56','r57','r58','r59','r599','r61','r62','r63','r64','r65','r68','r69','r71','r72','r73','r74','r75','r76','r77','r78','r79','r81','r82','r83','r84','r85','r87','r89','r91','r917','r92','r93','r94','r95','r96','r97','r99','s','t-','tb1','tb2','tb3','tb4','tb5','tb6','tb7','tb8','tb9','td','te','tf','tg1','tg2','tg3','tg4','tg5','tg7','tg8','tg9','th11','th12','th13','th14','th16','th17','th18','th2','th3','th4','th6','th7','tj','tk0','tk1','tk2','tk3','tk4','tk5','tk6','tk7','tk8','tk91','tn0','tn1','tn2','tn3','tn4','tn6','tn7','tn8','tn91','tn92','tn93','tn94','tn95','tn96','tn97','tn99','tp1','tp20','tp21','tp23','tp24','tp27','tp29','tp30','tp311','tp312','tp313','tp314', 'tp315', 'tp316', 'tp317', 'tp319', 'tp32', 'tp33', 'tp34', 'tp35', 'tp36', 'tp37', 'tp38', 'tp391', 'tp392', 'tp393', 'tp399', 'tq0', 'tq1', 'tq2', 'tq3', 'tq4', 'tq5', 'tq6', 'tq9', 't', 'tu-', 'tu1', 'tu19', 'tu2', 'tu3', 'tu4', 'tu5', 'tu6', 'tu7', 'tu6', 'tu9', 'tv', 'u', 'v', 'x1', 'x2', 'x3', 'x4', 'x5', 'x7', 'x8', '9', 'z']
    for i in range(len(mdzz_1)):
        start_url='http://ftp.lib.hust.edu.cn/search*chx?/c'+mdzz_1[i]
        html_1=getHTMLText(start_url)
        reg=re.compile(r'共有记录<br />  (.*?) 条',re.S)
        num_1=reg.findall(html_1)
        depth_1=int(num_1[0])
        depth=round(depth_1/50)
        for j in range(depth):
            try:
                infoList=[]
                Link=[]
                url=start_url+'/c'+mdzz_1[i]+'/'+str(50*j+1)+'%2C'+str(depth_1)+'%2C'+str(depth_1)+'%2CB/browse/indexsort=r'
                html=getHTMLText(url)
                infoList=parsePage(html)
                Link=parseLink(html)
                printDatabase(infoList)
                printDatabase_link(Link)
                print(mdzz_1[i]+":成功插入前"+str(50*j+50)+"条数据")
            except:
                print(mdzz_1[i]+':插入前'+str(50*j+50)+"条数据失败")
                continue
main()
