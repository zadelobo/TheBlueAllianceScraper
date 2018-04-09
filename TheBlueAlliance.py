def parseTableForCaptain (table):
	if (table == None):
		final = ['No Data', 'No Data', 'No Data']
	else:
		row = table.find_all('tr')[0]
		values = row.find("td", attrs={"class": "winnerC"})
		final = values.text.strip().splitlines()
	return final

def prepForFormatting (heading, teams):
	li = [heading]+teams
	final = ""
	for elem in li:
		final = final + elem + ","
	return final[:-1]

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
head_page = "https://www.thebluealliance.com/event/2018"
event_codes = ["abca","alhu","arli","ausc","ausp","azfl","azpx","bcvi","caav","cada","cafr","cair","capo","casd","casf","casj","cave","cmpmi","cmptx","code","cthar","ctsct","ctwat","flor","flwp","gaalb","gacol","gadal","gadul","gagai","gush","hiho","iacf","idbo","ilch","ilpe","inmis","inpla","inwla","isde1","isde2","isde3","isde4","lake","mabos","mabri","marea","mawor","mdedg","mdoxo","melew","mialp","mibel","micen","miesc","mifor","migay","migib","migul","mike2","miken","miket","milak","milan","milin","miliv","milsu","mimar","mimid","mimil","mishe","misjo","misou","mitry","mitvc","miwat","miwmi","mndu","mndu2","mnmi","mnmi2","mokc","mokc2","mosl","mxmo","mxto","ncash","ncgre","ncpem","ncwin","ndgf","nhdur","nhgrs","njbri","njfla","njski","njtab","nvlv","nyli","nyli2","nyny","nyro","nysu","nytr","nyut","ohcl","ohmv","okok","onbar","onham","onlon","onnob","onnyo","onosh","onto1","onwat","onwin","orlak","orore","orwil","paca","pahat","paphi","pawch","qcmo","rismi","scmb","shmi","tnkn","tuis","txda","txel","txho","txlu","txpa","txsa","utwv","vabla","vagdc","vagle","vahay","vapor","waahs","waamv","wamou","wasno","waspo","wayak","wila","wimi"]

for event_code in event_codes:
	quote_page = head_page + event_code + "#results"
	quote_page = Request(head_page + event_code + "#results", headers={'User-Agent': 'Mozilla/5.0'})
	page = urlopen(quote_page)
	soup = BeautifulSoup(page, "html.parser")
	title = soup.find("h1", attrs={"itemprop": "summary"})
	title = title.text.strip()
	title = title[:-5]
	bracket = soup.find("table", attrs={"class": "brackettable"})
	winningAlliance = parseTableForCaptain(bracket)
	print(prepForFormatting(title, winningAlliance))