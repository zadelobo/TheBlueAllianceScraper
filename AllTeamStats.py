def parseTableForAlliances (table, amount):
	final = []
	if (table == None):
		final = ['No Data', 'No Data', 'No Data', 'No Data', 'No Data', 'No Data', 'No Data', 'No Data', 'No Data']
	else:
		for rowindex in range(1,amount+1):
			row = table.find_all('tr')[rowindex]
			row = row.text.strip()
			row = row.replace("\n", "")
			row = " ".join(row.split())
			final.append(row)
	return final

def prepForFormatting (heading, teams, amount):
	for num in range(0,amount):
		f.write(title + "," + teams[num].replace(" ", ",") + "\n")

f = open('output.csv','w')
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
head_page = "https://www.thebluealliance.com/event/2018"
event_codes = ["abca","alhu","arli","ausc","ausp","azfl","azpx","bcvi","caav","cada","cafr","cair","capo","casd","casf","casj","cave","code","cthar","ctsct","ctwat","flor","flwp","gaalb","gacol","gadal","gadul","gagai","gush","hiho","iacf","idbo","ilch","ilpe","inmis","inpla","inwla","isde1","isde2","isde3","isde4","lake","mabos","mabri","marea","mawor","mdedg","mdoxo","melew","mialp","mibel","micen","miesc","mifor","migay","migib","migul","mike2","miken","miket","milak","milan","milin","miliv","milsu","mimar","mimid","mimil","mishe","misjo","misou","mitry","mitvc","miwat","miwmi","mndu","mndu2","mnmi","mnmi2","mokc","mokc2","mosl","mxmo","mxto","ncash","ncgre","ncpem","ncwin","ndgf","nhdur","nhgrs","njbri","njfla","njski","njtab","nvlv","nyli","nyli2","nyny","nyro","nysu","nytr","nyut","ohcl","ohmv","okok","onbar","onham","onlon","onnob","onnyo","onosh","onto1","onwat","onwin","orlak","orore","orwil","paca","pahat","paphi","pawch","qcmo","rismi","scmb","shmi","tnkn","tuis","txda","txel","txho","txlu","txpa","txsa","utwv","vabla","vagdc","vagle","vahay","vapor","waahs","waamv","wamou","wasno","waspo","wayak","wila","wimi"]
#event_codes = ["abca","alhu","nyli2","casj"]
ranks = [[],[],[],[],[],[],[],[]]
f.write("Regional,Rank,Team,Ranking Score,Park/Climb Points,Auto,Ownership,Vault,Record(W-L-T),DQ,Matches Played,Total Ranking Points\n")
count = 1
for event_code in event_codes:
	print("Finding Event "+str(count)+"/148")
	quote_page = Request(head_page + event_code + "#rankings", headers={'User-Agent': 'Mozilla/5.0'})
	page = urlopen(quote_page)
	soup = BeautifulSoup(page, "html.parser")
	title = soup.find("h1", attrs={"itemprop": "summary"})
	title = title.text.strip()
	title = title[:-5]
	table = soup.find("table", attrs={"id": "rankingsTable"})
	if (table==None):
		print("Skipped Event " + event_code + ": No Data Found")
		count +=1
		continue
	teams = table.find_all('tr')
	teams = len(teams)
	teams -= 1
	print("Found "+str(teams)+" teams")
	print("Copying information from Event "+str(count)+"/148: "+title+" Regional")
	topAlliances = parseTableForAlliances(table, teams)
	prepForFormatting(title,topAlliances,teams)
	count += 1
f.close()


