import json, time, urllib.request, csv
URL="https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch"
P=["boy mama","girl mama","dog mom","dog mama","dog dad","cat mom","cat mama","cool aunt","aunt life","nana","mimi","gigi","glamma","grandma est","grandma life","promoted to grandma","new grandma","baby's first christmas","our first christmas","first christmas married","our first home","officially retired","retired teacher","retired not my problem anymore","teacher off duty","teach love inspire","teacher life","nurse life","work bestie","reel cool","reel cool dad","crazy plant lady","plant lady","book lover","bookish","just one more chapter","book club","coffee lover","mama claus","merry and bright","mom est","dad est","grandpa est","girl dad","mama","grandma","retirement","coworker"]
REL={"IC 025","IC 021","IC 016","IC 020","IC 024","IC 014","IC 018","IC 028"}
rows=[]
for p in P:
    q={"query":{"bool":{"must":[{"match_phrase":{"WM":p}}]}},"size":200,"_source":["wordmark","alive","registered","statusDescription","internationalClass","ownerName","id","registrationId"]}
    req=urllib.request.Request(URL,data=json.dumps(q).encode(),headers={"Content-Type":"application/json","User-Agent":"Mozilla/5.0"})
    for a in range(3):
        try: d=json.load(urllib.request.urlopen(req,timeout=30)); break
        except Exception as e: time.sleep(3); d=None
    if not d: rows.append((p,"ERR","","","")); continue
    hits=[h["source"] for h in d["hits"]["hits"]]
    live=[h for h in hits if str(h.get("alive"))=="True" and REL & set(h.get("internationalClass") or [])]
    exact=[h for h in live if (h.get("wordmark") or "").strip().lower().replace("’","'")==p]
    ex="; ".join(f'{h["wordmark"]} [{",".join(c.replace("IC ","") for c in h["internationalClass"])}] {"REG" if str(h.get("registered"))=="True" else "PENDING"} #{h.get("registrationId") or h["id"]}' for h in exact[:4])
    others="; ".join(sorted({(h.get("wordmark") or "") for h in live if h not in exact})[:6])
    rows.append((p,d["hits"]["totalValue"],len(live),ex or "-",others or "-"))
    time.sleep(0.7)
with open("tm_results.csv","w",newline="") as f: csv.writer(f).writerows([("phrase","total_hits","live_in_product_classes","exact_live_marks","other_live_containing")]+rows)
for r in rows: print(" | ".join(str(x) for x in r))
