import time, json
from pytrends.request import TrendReq
t=TrendReq(hl="en-US",tz=300,timeout=(10,30))
seeds=["personalized ornament","custom sweatshirt","custom mug","personalized blanket","custom tumbler","pet portrait","boss gift","coworker gift","fishing gift","grandma gift","teacher gift","retirement gift","nurse gift","gardening gift","mama sweatshirt"]
out={}
for s in seeds:
    for a in range(3):
        try:
            t.build_payload([s],timeframe="today 3-m",geo="US"); rq=t.related_queries()[s]
            out[s]={k:(v.head(15).values.tolist() if v is not None else []) for k,v in rq.items()}
            print("ok",s,flush=True); break
        except Exception as e: print("retry",s,e,flush=True); time.sleep(30*(a+1))
    time.sleep(10)
json.dump(out,open("rising.json","w"),indent=1)
