---
title: "Automated Business Cycle Dashboard"
author: ["Pascal Michaillat","Emmanuel Saez"]
description: "This dashboard provides real-time charts on US unemployment rate, vacancy rate, labor market tightness, FERU, unemployment gap, and recession probability."
cover:
    image: "/dashboard.png"
    alt: "US recession probability from dual-threshold Michez rule"
editPost:
    URL: "https://pascalmichaillat.org/18/"
    Text: "Theoretical foundations and policy implications"
showToc: true
disableAnchoredHeadings: false

---

This dashboard provides real-time indicators of labor market slack and business cycle conditions in the United States. All charts automatically update as new data become [available on FRED](https://fred.stlouisfed.org/).

---

## US unemployment rate

<iframe
    src="/dashboard/unemployment_rate.html"
    title="US unemployment rate"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ [View in full screen](/dashboard/unemployment_rate.html)
+ [Download unemployment rate](/dashboard/unemployment_rate.csv)
+ *Construction* - The unemployment rate is the number of job seekers divided by the number of labor force participants.
+ *Interpretation* - The unemployment rate measures the share of people who have not succeeded in finding a job, among all those who are available and willing to work. This is the standard, official unemployment rate (U3).
+ *Source* - The numbers of [job seekers](https://fred.stlouisfed.org/series/UNEMPLOY) and [labor force participants](https://fred.stlouisfed.org/series/CLF16OV) are measured by the US Bureau of Labor Statistics (BLS) from the [Current Population Survey](https://www.bls.gov/cps/home.htm) (CPS), which is a large-scale household survey. 

---

## US vacancy rate

<iframe
    src="/dashboard/vacancy_rate.html"
    title="US vacancy rate"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ [View in full screen](/dashboard/vacancy_rate.html)
+ [Download vacancy rate](/dashboard/vacancy_rate.csv)
+ *Construction* - The vacancy rate is the number of job openings divided by the number of labor force participants. 
+ *Interpretation* - The vacancy rate measures the number of job openings per labor force participant. 
+ *Source* - The number of [job openings](https://fred.stlouisfed.org/series/JTSJOL) is measured by the BLS from the [Job Openings and Labor Turnover Survey](https://www.bls.gov/jlt/) (JOLTS), which is a large-scale firm survey.

---

## US labor market tightness

<iframe
    src="/dashboard/labor_market_tightness.html"
    title="US labor market tightness"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ [View in full screen](/dashboard/labor_market_tightness.html)
+ [Download labor market tightness](/dashboard/labor_market_tightness.csv)
+ *Construction* - Labor market tightness is the vacancy rate divided by the unemployment rate. 
+ *Interpretation* - Labor market tightness measures the number of job openings per job seeker. A tightness of 1 marks full employment, or equivalently labor market efficiency. When tightness is below 1, the labor market is inefficiently slack. When tightness is above 1, the labor market is inefficiently tight.
+ *Source* - [Michaillat and Saez (2024)](/13/)

---

## US Beveridge curve

<iframe
    src="/dashboard/beveridge_curve.html"
    title="US Beveridge curve"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ [View in full screen](/dashboard/beveridge_curve.html)
+ *Construction* - The Beveridge curve is a scatter plot of the vacancy rate against the unemployment rate. 
+ *Interpretation* - The Beveridge curve is one of the most robust relationships in macroeconomics. During business cycles, the economy moves along the Beveridge curve. In recessions the unemployment rate increases while the vacancy rate decreases; in expansions the unemployment rate decreases while the vacancy rate increases. Since the economy is at full employment when the unemployment and vacancy rates are equal, the economy is inefficiently tight when it is above the 45° ray and inefficiently slack when it is below the 45° ray.
+ *Source* - [Michaillat and Saez (2024)](/13/)

---

## US full-employment rate of unemployment (FERU)

<iframe 
    src="/dashboard/feru.html"
    title="US full-employment rate of unemployment (FERU)"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ [View in full screen](/dashboard/feru.html)
+ [Download FERU](/dashboard/feru.csv)
+ *Construction* - The FERU ($u^\ast$) is the geometric average of the unemployment rate ($u$) and vacancy rate ($v$): $u^\ast = \sqrt{u \times v}$. 
+ *Interpretation* - The FERU marks full employment. The [1946 Employment Act](https://fraser.stlouisfed.org/title/1099) and [1978 Full Employment and Balanced Growth Act](https://fraser.stlouisfed.org/title/1034) state that achieving full employment is a way to maximize social welfare. So we compute the FERU as the unemployment rate that maximizes social welfare by minimizing socially unproductive uses of labor—both job seeking and recruiting. By construction, therefore, the FERU is also the efficient unemployment rate.
+ *Visualization* - On the Beveridge diagram, the FERU is at the intersection of the Beveridge curve and the 45° ray. The FERU is therefore determined by the location of the Beveridge curve: it is higher when the Beveridge curve is further outward.
+ *Source* - [Michaillat and Saez (2024)](/13/)

---

## US unemployment gap

<iframe 
    src="/dashboard/unemployment_gap.html"
    title="US unemployment gap"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ [View in full screen](/dashboard/unemployment_gap.html)
+ [Download unemployment gap](/dashboard/unemployment_gap.csv)
+ *Construction* - The unemployment gap is the distance $u - u^\ast$ between the actual unemployment rate ($u$) and the FERU ($u^\ast$). 
+ *Interpretation* - The unemployment gap indicates the distance from full employment. A positive gap marks an inefficiently slack labor market. A negative gap marks an inefficiently tight labor market. The unemployment gap is a key determinant of optimal monetary and fiscal policy.
+ *Source* - [Michaillat and Saez (2024)](/13/)

---

## US recession indicator

<iframe 
    src="/dashboard/recession_indicator.html" 
    title="US recession indicator"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ [View in full screen](/dashboard/recession_indicator.html)
+ [Download recession indicator](/dashboard/recession_indicator.csv)
+ *Construction* - The recession indicator is the minimum of two indicators. The first is the unemployment indicator from the Sahm rule: the increase in the 3-month average of the unemployment rate above its 12-month low ([view](/dashboard/unemployment_indicator.html) or [download](/dashboard/unemployment_indicator.csv) that indicator). The second is a vacancy indicator constructed analogously: the decrease in the 3-month average of the vacancy rate below its 12-month high ([view](/dashboard/vacancy_indicator.html) or [download](/dashboard/vacancy_indicator.csv) that indicator).
+ *Interpretation* - The Michez rule signals a recession whenever the recession indicator is above the threshold of 0.29pp. The detected recession start date is the month when the indicator crosses the 0.29pp threshold from below.
+ *Source* - [Michaillat and Saez (2025)](/16/)

---

## US recession probability

<iframe 
    src="/dashboard/recession_probability.html" 
    title="US recession probability"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ [View in full screen](/dashboard/recession_probability.html)
+ [Download recession probability](/dashboard/recession_probability.csv)
+ *Construction* - The recession probability is computed from the dual-threshold extension of the Michez rule. The recession probability is the fraction of the 0.29pp–0.81pp range that the recession indicator has covered: $p =$ (indicator $-$ 0.29) $/$ (0.81 $-$ 0.29).
+ *Interpretation* - The dual-threshold Michez rule works as follows: values of the indicator below 0.29pp signal no recession; values between 0.29pp and 0.81pp signal a probable recession; values above 0.81pp signal a certain recession. The dual-threshold extension accounts for uncertainty in the true recession threshold and provides a simple way to nowcast recession risk. 
+ *Source* - [Michaillat and Saez (2025)](/16/)

---

## Frequently asked questions

### When do the numbers for the current month become available?

The data required to populate the dashboard for a given month are released by the BLS in the first week of the following month, usually on a Tuesday for the JOLTS data and on a Friday for the CPS data:

+ Latest [JOLTS data release](https://www.bls.gov/news.release/jolts.nr0.htm)
+ Latest [CPS data release](https://www.bls.gov/news.release/empsit.nr0.htm)

Accordingly, the dashboard usually provides a complete picture for the current month on the first Friday of the following month. The schedule of [future data releases](https://www.bls.gov/schedule/) is announced well in advance by the BLS.

The JOLTS data for a given month appear to be released one month after the CPS data for the same month, but to best align labor force and vacancy data, we shift forward by one month the number of job openings from JOLTS. For instance, we assign to April 2025 the number of job openings that the BLS assigns to March 2025. The motivation for this shift is that the number of job openings from the JOLTS refers [to the last business day](https://perma.cc/Y6EQ-WBXF) of the month (Monday 31 March 2025), while the labor force from the CPS refers to the Sunday–Saturday week [including the 12th of the month](https://perma.cc/RN3P-S4SL) (Sunday 6 April 2025–Saturday 12 April 2025). So the number of job openings refers to a day that is closer to the next month's CPS reference week than to the current month's CPS reference week. In 2025, the CPS survey for April started in the same week as the JOLTS survey for March.

### Are the numbers final upon release? Or will they be revised?

The numbers constructed in real time might not be final because the unemployment, vacancy, and labor force data are revised by the BLS after their initial release:

+ The number of job openings released by the BLS is preliminary and updated one month after its initial release, to incorporate additional survey responses received from businesses and government agencies and from the recalculation of seasonal factors. 
+ The BLS revises the prior five years of CPS and JOLTS data each year at the beginning of January, to account for revisions to seasonal factors, population estimates, and employment estimates.

Yet, revisions to labor market data are generally minimal, especially compared to GDP revisions, so the information provided by labor market data in real time  is [generally indistinguishable](https://perma.cc/W79A-EFPF) from the information provided in the final version.

### Why are there no data for October 2025?

The US government was shut down between 10/01/2025 and 11/12/2025, which [seriously affected the collection of labor market data](https://www.bls.gov/cps/methods/2025-federal-government-shutdown-impact-cps.htm). The October 2025 wave of the CPS was not collected, so there will be no unemployment and labor force estimates for that month. Accordingly, the dashboard cannot provide data for October 2025.

### Is the unemployment rate the same as the BLS unemployment rate?

Yes, almost. The two unemployment rates are computed similarly, but the BLS reports the [unemployment rate](https://fred.stlouisfed.org/series/UNRATE) with one-digit precision, while the dashboard reports it with two-digit (basis-point) precision. This higher precision is useful for recession detection, as recession indicators are computed at the basis-point level.

### Is the vacancy rate the same as the BLS vacancy rate?

No. The BLS computes the [vacancy rate](https://fred.stlouisfed.org/series/JTSJOR) as the number of job vacancies divided by the number of employed workers plus job openings. This computation is problematic for two reasons. First, it means that the BLS unemployment and vacancy rates are not consistent with each other, since one uses the number of employed workers plus unemployed workers in the denominator, while the other uses the number of employed workers plus job openings in the denominator. Second, the BLS vacancy rate is not a useful variable in labor market models.

By contrast, the dashboard computes the vacancy rate as the number of job vacancies divided by the number of employed workers plus unemployed workers. Our unemployment and vacancy rates are consistent with each other, and our vacancy rate is the variable that appears directly in models.

### Isn't the vacancy rate distorted by ghost job postings?

A [recent article](https://perma.cc/JUR9-W4AA) by CBS News explains that ghost job postings—which do not represent open positions and will not lead to new hires—are a growing problem in online job boards. As the vacancy numbers on the dashboard come from the BLS and not from online job boards, however, they are immune to this problem.

Specifically, the [BLS asks firms to report](https://www.bls.gov/jlt/jltc1.pdf) the number of vacancies that they currently have, where a vacancy is defined as follows:

+ A specific position exists and work is available.
+ The job could start within 30 days.
+ The firm is actively recruiting workers from the outside to fill the position.

These questions are similar to the questions asked by the BLS to workers in order to assess their labor force status, so the bar for reporting a job vacancy is as high as the bar for being counted as a job seeker. 

### Why is the FERU not constant?

The FERU describes the socially efficient position of the labor market on the Beveridge curve, so it is not constant but determined by the location of the Beveridge curve. When the Beveridge curve shifts outward, the FERU increases; when the Beveridge curve shifts inward, the FERU decreases. Typical Beveridge curve shifts do not affect the FERU much. For instance, between 1951 and 2019, the FERU remained broadly between 3% and 5.5%. The Beveridge curve did shift in and out during the postwar period, but the shifts were not large enough to produce noteworthy changes in the FERU. 

During the coronavirus pandemic, the Beveridge curve shifted out dramatically, which raised the FERU significantly. As the Beveridge curve normalized in the years after the pandemic, the FERU returned to normal levels. The FERU increase that followed the pandemic is extraordinary: the pandemic is the first time in the past century that the FERU crossed 6%.

### How does the Michez rule relate to the Sahm rule?

The Michez rule is based on the same idea as the Sahm rule: looking for a rapid deterioration of the labor market to detect recessions. But while the Sahm rule only uses the unemployment rate for detection, the Michez rule uses both unemployment and vacancy rates. By combining data on unemployment and vacancies, the Michez rule obtains a less noisy signal of recessions, so it can detect recessions faster than the Sahm rule: 

+ Average detection delay, 1960–2021: 1.2 months < 2.7 months
+ Maximum detection delay, 1960–2021: 3 months < 7 months

The Michez rule is also more robust: it identifies all 15 recessions since 1929 without false positives, whereas the Sahm rule breaks down before 1960.