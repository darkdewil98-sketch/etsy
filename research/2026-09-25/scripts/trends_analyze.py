import pandas as pd, json
c=pd.read_csv("trends_clean.csv",header=[0,1],index_col=0,parse_dates=True)
d=pd.read_csv("trends_5y.csv",header=[0,1],index_col=0,parse_dates=True).iloc[:-1]
A="custom sweatshirt"
def m(x,a,b): return x[a:b].mean()
base=m(c[("formats",A)],"2023-01-01","2025-12-31")
rows=[]
for g in c.columns.levels[0]:
    sub=c[g]; s=m(sub[A],"2023-01-01","2025-12-31")/base
    for k in sub.columns:
        if k==A and g!="formats": continue
        x=sub[k]*s/base*100
        q3=m(x,"2025-07-01","2025-09-30"); hol=m(x,"2025-11-01","2025-12-31")
        pk=[x[str(y)].idxmax() for y in (2022,2023,2024,2025)]
        # ramp: first week in 2025 H2 where value >= 2x Q3 average
        h2=x["2025-09-01":"2025-12-31"]; ramp=h2[h2>=2*q3].index.min() if q3>0 else None
        y=d[g][k]; q26=m(y,"2026-07-01","2026-09-19"); q25=m(y,"2025-07-01","2025-09-20")
        rows.append(dict(keyword=k,group=g,idx_2023_25=round(m(x,"2023-01-01","2025-12-31")),
          y2025_vs_2024_pct=round((m(x,"2025-01-01","2025-12-31")/m(x,"2024-01-01","2024-12-31")-1)*100) if m(x,"2024","2024")>0 else None,
          novdec_x_q3=round(hol/q3,1) if q3>0 else None,
          peak_weeks="/".join(p.strftime("%m-%d") for p in pk),
          ramp_2x_2025=ramp.strftime("%m-%d") if ramp is not None and pd.notna(ramp) else "-",
          q3_26_vs_q3_25_pct=round((q26/q25-1)*100) if q25>0 else None,
          raw_group_median_2025=int(sub[k]["2025"].median())))
r=pd.DataFrame(rows).sort_values("idx_2023_25",ascending=False)
pd.set_option("display.width",250); print(r.to_string(index=False)); r.to_csv("trends_summary.csv",index=False)
