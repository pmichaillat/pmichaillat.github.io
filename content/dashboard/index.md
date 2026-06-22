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

This dashboard provides real-time indicators of US labor market and business cycle conditions. 

It starts with three core US labor market indicators: unemployment rate, vacancy rate, and labor market tightness. These metrics jointly characterize the functioning of the labor market. The dashboard also plots the Beveridge curve, which relates the unemployment and vacancy rates.

From these, the dashboard calculates two metrics that quantify how far the US labor market is from social efficiency: the full-employment rate of unemployment (FERU) and the unemployment gap. These metrics are key determinants of optimal monetary and fiscal policy.

Finally, the dashboard presents two metrics that signal the risk that the US economy has entered a recession: the Michez-rule recession indicator and the Michez-rule recession probability. These metrics provide early signs of labor market weakening and signal upcoming deterioration.

All charts automatically update as new data become [available on FRED](https://fred.stlouisfed.org/), providing a real-time view of the US business cycle.

---

## Key events

+ November 2025 - The US government was shut down between 10/01/2025 and 11/12/2025, which [seriously affected the collection of labor market data](https://www.bls.gov/cps/methods/2025-federal-government-shutdown-impact-cps.htm). The September 2025 wave of the Current Population Survey (CPS)—which is the source of the unemployment and labor force numbers—was collected normally but published late, on 11/20/2025. The October 2025 wave of the CPS was not collected and will not be collected retroactively. So there will be no unemployment and labor force estimates for October 2025. Accordingly, the dashboard does not provide data for October 2025.
+ September 2025 - The Federal Reserve [cuts the federal funds rate by 25 basis points](https://www.federalreserve.gov/monetarypolicy/files/monetary20250917a1.pdf) in response to the cooling of the labor market.
+ August 2025 - The US labor market [dips below full employment](#us-unemployment-gap) for the first time since April 2021.
+ May 2025 - The dashboard is live.

---

## US unemployment rate

<iframe
    src="/dashboard/unemployment_rate.html"
    title="US unemployment rate"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ *Construction* - The unemployment rate is the number of job seekers divided by the number of labor force participants.
+ *Interpretation* - The unemployment rate measures the share of people who have not succeeded in finding a job, among all those who are available and willing to work. This is the standard, official unemployment rate (U3).
+ [Download unemployment rate](/dashboard/unemployment_rate.csv)
+ [View unemployment rate in full screen](/dashboard/unemployment_rate.html)
+ *Source* - The numbers of [job seekers](https://fred.stlouisfed.org/series/UNEMPLOY) and [labor force participants](https://fred.stlouisfed.org/series/CLF16OV) are measured by the US Bureau of Labor Statistics (BLS) from the [Current Population Survey](https://www.bls.gov/cps/home.htm) (CPS), which is a large-scale household survey. 

---

## US vacancy rate

<iframe
    src="/dashboard/vacancy_rate.html"
    title="US vacancy rate"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ *Construction* - The vacancy rate is the number of job openings divided by the number of labor force participants. 
+ *Interpretation* - The vacancy rate measures the number of job openings per labor force participant. 
+ [Download vacancy rate](/dashboard/vacancy_rate.csv)
+ [View vacancy rate in full screen](/dashboard/vacancy_rate.html)
+ *Source* - The number of [job openings](https://fred.stlouisfed.org/series/JTSJOL) is measured by the BLS from the [Job Openings and Labor Turnover Survey](https://www.bls.gov/jlt/) (JOLTS), which is a large-scale firm survey.

---

## US labor market tightness

<iframe
    src="/dashboard/labor_market_tightness.html"
    title="US labor market tightness"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ *Construction* - Labor market tightness is the vacancy rate divided by the unemployment rate. 
+ *Interpretation* - Labor market tightness measures the number of job openings per job seeker. A tightness of 1 marks full employment, or equivalently labor market efficiency. When tightness is below 1, the labor market is inefficiently slack. When tightness is above 1, the labor market is inefficiently tight.
+ [Download labor market tightness](/dashboard/labor_market_tightness.csv)
+ [View labor market tightness in full screen](/dashboard/labor_market_tightness.html)
+ *Source* - [Michaillat and Saez (2024)](/13/)

---

## US Beveridge curve

<iframe
    src="/dashboard/beveridge_curve.html"
    title="US Beveridge curve"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ *Construction* - The Beveridge curve links the unemployment rate to the vacancy rate. 
+ *Interpretation* - The Beveridge curve is one of the most robust relationships in macroeconomics. During business cycles, the economy moves along the Beveridge curve. In recessions the unemployment rate increases while the vacancy rate decreases; in expansions the unemployment rate decreases while the vacancy rate increases. Finally, since the economy is at full employment whenever the unemployment and vacancy rates are equal, the economy is inefficiently tight whenever it is above the 45° ray and inefficiently slack whenever it is below the 45° ray.
+ [View Beveridge curve in full screen](/dashboard/beveridge_curve.html)
+ *Source* - [Michaillat and Saez (2024)](/13/)

---

## US full-employment rate of unemployment (FERU)

<iframe 
    src="/dashboard/feru.html"
    title="US full-employment rate of unemployment (FERU)"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ *Construction* - The full-employment rate of unemployment (FERU) is the geometric average of the unemployment and vacancy rates: $u^\ast = \sqrt{u \times v}$, where $u$ is the unemployment rate, $v$ is the vacancy rate, and $u^\ast$ is the FERU. 
+ *Interpretation* - The FERU marks full employment. The [1946 Employment Act](https://fraser.stlouisfed.org/title/1099) of 1946 and [1978 Full Employment and Balanced Growth Act](https://fraser.stlouisfed.org/title/1034) state that achieving full employment is a way to maximize social welfare. So we compute the FERU as the unemployment rate that is socially efficient: it maximizes social welfare by minimizing socially unproductive uses of labor—both jobseeking and recruiting. The computation yields the formula $u^\ast = \sqrt{uv}$, and tells us that the FERU is also the socially efficient unemployment rate.
+ *Visualization* - On the Beveridge diagram, the FERU is at the intersection of the Beveridge curve and the 45° ray. The implication is that the FERU is determined by the location of the Beveridge curve: it is higher whenever the Beveridge curve is further outward.
+ [Download FERU](/dashboard/feru.csv)
+ [View FERU in full screen](/dashboard/feru.html)
+ *Source* - [Michaillat and Saez (2024)](/13/)

---

## US unemployment gap

<iframe 
    src="/dashboard/unemployment_gap.html"
    title="US unemployment gap"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ *Construction* - The unemployment gap is given by $u - u^\ast$, where $u$ is the unemployment rate and $u^\ast$ is the FERU. 
+ *Interpretation* - The unemployment gap indicates the distance from full employment. A positive gap marks an inefficiently slack labor market. A negative gap marks an inefficiently tight labor market.
+ [Download unemployment gap](/dashboard/unemployment_gap.csv)
+ [View unemployment gap in full screen](/dashboard/unemployment_gap.html)
+ *Source* - [Michaillat and Saez (2024)](/13/)

---

## US recession indicator

<iframe 
    src="/dashboard/recession_indicator.html" 
    title="US recession indicator"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ *Construction* - The recession indicator is the minimum of two indicators: an unemployment indicator constructed as the increase in the 3-month average of the unemployment rate above its 12-month low (used in Sahm rule); and a vacancy indicator constructed analogously as the decrease in the 3-month average of the vacancy rate below its 12-month high.
+ *Interpretation* - The Michez rule signals a recession when the recession indicator crosses the threshold of 0.29pp from below.
+ [Download recession indicator](/dashboard/recession_indicator.csv)
    + [Download underlying unemployment (Sahm) indicator](/dashboard/unemployment_indicator.csv)
    + [Download underlying vacancy indicator](/dashboard/vacancy_indicator.csv)
+ [View recession indicator in full screen](/dashboard/recession_indicator.html)
    + [View underlying unemployment (Sahm) indicator](/dashboard/unemployment_indicator.html)
    + [View underlying vacancy indicator](/dashboard/vacancy_indicator.html)
+ *Source* - [Michaillat and Saez (2025)](/16/)

---

## US recession probability

<iframe 
    src="/dashboard/recession_probability.html" 
    title="US recession probability"
    style="width: 100%; aspect-ratio: 4 / 3; border: none;">
</iframe>

+ *Construction* - The recession probability is computed from the dual-threshold extension of the Michez rule. The recession probability is the fraction of the 0.29pp–0.81pp range that the recession indicator has covered: $p =$ (indicator $-$ 0.29) $/$ (0.81 $-$ 0.29).
+ *Interpretation* - The dual-threshold Michez rule works as follows: values of the indicator between 0.29pp and 0.81pp signal a probable recession; values above 0.81pp signal a certain recession. The dual-threshold extension accounts for uncertainty in the true recession threshold and provides a simple way to nowcast recession risk. 
+ [Download recession probability](/dashboard/recession_probability.csv)
+ [View recession probability in full screen](/dashboard/recession_probability.html)
+ *Source* - [Michaillat and Saez (2025)](/16/)

---

## Frequently asked data questions

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

Yet, revisions to labor market data are generally minimal, especially compared to GDP revisions, so the information provided in real time by labor market data is generally [indistinguishable](https://perma.cc/W79A-EFPF) from the information provided in the final version.

### Is the unemployment rate the same as the BLS unemployment rate?

Yes, almost. The two unemployment rates are computed similarly, but the BLS reports the [unemployment rate](https://fred.stlouisfed.org/series/UNRATE) with one-digit precision, while the dashboard reports it with two-digit (basis-point) precision. This higher precision is useful for recession detection, as recession indicators are computed and reported at the basis-point level.

### Is the vacancy rate the same as the BLS vacancy rate?

No. The BLS computes the [vacancy rate](https://fred.stlouisfed.org/series/JTSJOR) as the number of job vacancies divided by the number of employed workers plus job openings. This computation is problematic for two reasons. First, it means that the BLS unemployment and vacancy rates are not consistent with each other, since one uses the number of employed workers plus unemployed workers in the denominator, while the other uses the number of employed workers plus job openings in the denominator. Second, the BLS vacancy rate is not a useful variable in labor market matching models.

By contrast, the dashboard computes the vacancy rate as the number of job vacancies divided by the number of employed workers plus unemployed workers. Our unemployment and vacancy rates are consistent with each other. Furthermore, our vacancy rate is the variable that appears directly in labor market matching models.

### How does the Michez rule relate to the Sahm rule?

The Michez rule is based on the same idea as the Sahm rule: looking for a rapid deterioration of labor market variables to detect recessions. But while the Sahm rule only uses the unemployment rate for detection, the Michez rule uses both the unemployment and vacancy rates. 

By combining data on unemployment and vacancies, the Michez rule obtains a less noisy signal of recessions, so it can detect recessions faster than the Sahm rule: 

+ Average detection delay, 1960–2021: 1.2 months < 2.7 months
+ Maximum detection delay, 1960–2021: 3 months < 7 months

The Michez rule is also more robust: it identifies all 15 recessions since 1929 without false positives, whereas the Sahm rule breaks down before 1960.

### Is the FERU the same as the NAIRU?

No. In recent times, the US government has used the non-accelerating-inflation rate of unemployment (NAIRU) as full-employment target. For instance, the Joint Economic Committee [recently wrote](https://perma.cc/E9V8-XTFH):

> Today, full employment is considered by many to be synonymous with the non-accelerating inflationary rate of unemployment (NAIRU)—the rate of unemployment that neither stokes nor slows inflation.

Similarly, in 2024, the Council of Economic Advisers described the concept of full employment [as follows](https://perma.cc/2JGM-QG4Z): 

> Modern economics has generally defined full employment by citing the theoretical concept of the lowest unemployment rate consistent with stable inflation, which is referred to as $u^\ast$, the non-accelerating inflationary rate of unemployment (termed NAIRU).

These quotes are particularly meaningful because the Joint Economic Committee and Council of Economic Advisers were both created by the Employment Act of 1946 to ensure that the government achieved its full-employment mandate.

But this is a misconception: the NAIRU is an entirely different concept than the FERU. The FERU is the socially efficient unemployment rate. The NAIRU is the unemployment rate at which inflation remains stable. Since there is no guarantee that the unemployment rate prevailing under stable inflation is efficient, there is no guarantee that the NAIRU and FERU are the same.

### Is the FERU the same as the CBO's NRU?

Another full-employment target used by the US government is the natural rate of unemployment (NRU)—recently rebranded noncyclical rate of unemployment—constructed by the Congressional Budget Office (CBO). The CBO's NRU is a [slow-moving trend](https://perma.cc/NU5V-8ZY4) of the unemployment rate computed by assuming that the labor market was at full employment in 2005 and then incorporating changes in the demographic composition of the labor force over time. 

But, without a theory of full employment, it is impossible to know whether the US labor market really was at full employment in 2005, and by induction, whether the NRU in any year measures full employment. The NRU can therefore not be a satisfactory measure of full employment.

### Why is the FERU not constant?

The FERU is computed as the unemployment rate that maximizes social welfare, or equivalently that minimizes the nonproductive use of labor: both unemployment and recruiting. As it takes one worker to service one job vacancy, the nonproductive use of labor is measured by the number of job seekers and job vacancies. Through the Beveridge curve, the numbers of job seekers and vacancies are inversely related, so it is not possible to reduce the numbers of job seekers and job vacancies at the same time. Instead the social planner faces a tradeoff which is resolved by the FERU.

Because the FERU describes the socially efficient position of the labor market on the Beveridge curve, it is not constant but determined by the location of the Beveridge curve. When the Beveridge curve shifts outward, the FERU increases; when the Beveridge curve shifts inward, the FERU decreases. Typical Beveridge curve shifts do not affect the FERU much. For instance, between 1951 and 2019, the FERU remained between 3.1% and 5.5%, with an average value of 4.3%. The Beveridge curve did shift in and out during the postwar period, but the shifts were not large enough to produce noteworthy changes in the FERU. 

During the coronavirus pandemic, the Beveridge curve shifted out dramatically. The Beveridge curve then slowly shifted back inward. In 2025, the curve is almost back to its pre-pandemic position, although it remains somewhat further out. The dramatic shift raised the FERU significantly: from 3.8% in January 2020 to 7.5% in April 2020. As the Beveridge curve normalized in the years after the pandemic, the FERU returned to normal levels. The FERU increase that followed the pandemic is extraordinary: such a large increase had never been recorded before. The pandemic was also the first time in the past century that the FERU crossed 6%.
