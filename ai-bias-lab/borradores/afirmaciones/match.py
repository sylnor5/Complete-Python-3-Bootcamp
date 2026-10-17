import json,re,sys,unicodedata
def norm(t):
    t=unicodedata.normalize("NFKD",t);t="".join(ch for ch in t if not unicodedata.combining(ch))
    t=t.lower().replace("’","'").replace("‘","'").replace("´","'").replace("״",'"').replace("“",'"').replace("”",'"')
    return re.sub(r"\s+"," ",t)
cb=json.load(open(sys.argv[1]))
for f in sys.argv[2:]:
    txt=norm(open(f).read());hits=[]
    for c in cb["claims"]:
        m=[]
        for lang,ts in c["triggers"].items():
            for t in ts:
                if t.startswith("re:"):
                    if re.search(norm(t[3:]),txt): m.append(t)
                elif norm(t) in txt: m.append(t)
        if m: hits.append((c["side"][0].upper(),c["id"],m[:3]))
    print("==",f.split("/")[-1]);[print(" ",*h) for h in hits]
