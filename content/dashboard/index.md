---
title: "Automated Business Cycle Dashboard"
tags: ["business cycle", "FERU", "job vacancies", "labor market tightness", "Michez rule", "recession indicator", "recession probability", "recessions", "unemployment", "unemployment gap"]
author: ["Pascal Michaillat","Emmanuel Saez"]
description: "A dashboard with real-time charts on US unemployment rate, vacancy rate, labor market tightness, FERU, unemployment gap, and recession probability."
cover:
    image: "/dashboard.png"
    alt: "US recession probability from dual-threshold Michez rule"
    relative: false
editPost:
    URL: "https://github.com/pmichaillat/pmichaillat.github.io/tree/main/content/dashboard"
    Text: "Source code"
showToc: true
disableAnchoredHeadings: false

---

## US unemployment rate

<iframe src="/dashboard/unemployment_rate.html" style="width: 100%; aspect-ratio: 4 / 3; border: none;"></iframe>

The unemployment rate is the number of job seekers divided by the number of labor force participants. It measures the share of the labor force that is unemployed. The numbers of job seekers and labor force participants are both measured by the US Bureau of Labor Statistics (BLS) from the Current Population Survey (CPS), which is a large-scale household survey. 

## US vacancy rate

<iframe src="/dashboard/vacancy_rate.html" style="width: 100%; aspect-ratio: 4 / 3; border: none;"></iframe>

The vacancy rate is the number of job openings divided by the number of labor force participants. It measures the number of job openings per labor force participant. The number of job openings is measured by the BLS from the Job Openings and Labor Turnover Survey (JOLTS), which is a large-scale firm survey.


## US labor market tightness


<iframe src="/dashboard/labor_market_tightness.html" style="width: 100%; aspect-ratio: 4 / 3; border: none;"></iframe>

Labor market tightness is the vacancy rate divided by the unemployment rate. It measures the number of job openings per job seeker. A tightness of 1 marks full employment, or equivalently labor market efficiency. When tightness is below 1, the labor market is inefficiently slack. When tightness is above 1, the labor market is inefficiently tight.

## US full-employment rate of unemployment (FERU)

<iframe src="/dashboard/feru.html" style="width: 100%; aspect-ratio: 4 / 3; border: none;"></iframe>

The full-employment rate of unemployment (FERU) is the geometric average of the unemployment and vacancy rates: $u^\ast = \sqrt{u \times v}$, where $u$ is the unemployment rate, $v$ is the vacancy rate, and $u^\ast$ is the FERU. The FERU marks full employment and, by construction, labor market efficiency.

## US unemployment gap

<iframe src="/dashboard/unemployment_gap.html" style="width: 100%; aspect-ratio: 4 / 3; border: none;"></iframe>

The unemployment gap is given by $u - u^\ast$, where $u$ is the unemployment rate and $u^\ast$ is the FERU. The unemployment gap indicates the distance from full employment. A positive gap marks an inefficiently slack labor market. A negative gap marks an inefficiently tight labor market.

## US recession indicator

<iframe src="/dashboard/recession_indicator.html" style="width: 100%; aspect-ratio: 4 / 3; border: none;"></iframe>

The recession indicator is the minimum of the Sahm-rule indicator (the increase of the 3-month average of the unemployment rate above its 12-month low) and a vacancy analogue (the decrease of the 3-month average of the vacancy rate below its 12-month high). The Michez rule signals a recession when the indicator crosses the threshold of 0.29pp.

## US recession probability

<iframe src="/dashboard/recession_probability.html" style="width: 100%; aspect-ratio: 4 / 3; border: none;"></iframe>

The recession probability is computed from the dual-threshold extension of the Michez rule. The dual-threshold rule works as follows: values of the indicator between 0.29pp and 0.81pp signal a probable recession; values above 0.81pp signal a certain recession. This dual-threshold extension accounts for uncertainty in the true recession threshold and provides a simple way to nowcast recession risk. The recession probability is the fraction of the 0.29pp–0.81pp band that the indicator has covered.

---

## Download data (CSV)

+ [Unemployment rate](/dashboard/unemployment_rate.csv)
+ [Vacancy rate](/dashboard/vacancy_rate.csv)
+ [Labor market tightness](/dashboard/labor_market_tightness.csv)
+ [Full-employment rate of unemployment (FERU)](/dashboard/feru.csv)
+ [Unemployment gap](/dashboard/unemployment_gap.csv)
+ [Recession indicator](/dashboard/recession_indicator.csv)
+ [Recession probability](/dashboard/recession_probability.csv)

---

## Frequently asked questions

### When do the numbers for the current month become available?

The data required to populate the dashboard for any given month are released in the first week of the following month, usually [on a Tuesday for the JOLTS data and on a Friday for the CPS data](https://www.bls.gov/schedule/2025/home.htm). Accordingly, the dashboard will usually provide a complete picture for the current month on the first Friday of the following month.

It does appear that the JOLTS data for a given month are released one month after the CPS data for the same month, but to best align labor force and vacancy data, we shift forward by one month the number of job openings from JOLTS. For instance, we assign to December 2023 the number of job openings that the BLS assigns to November 2023. The motivation for this shift is that the number of job openings from the JOLTS refers to the last business day of the month (Thursday 30 November, 2023), while the labor force from the CPS refers to the Sunday--Saturday week including the 12th of the month (Sunday 10 December 2023 to Saturday 16 December 2023). So the number of job openings refers to a day that is closer to the next month's CPS reference week than to the current month's CPS reference week. Another advantage of shifting forward by one month the number of job openings from the JOLTS is that we have access to the data required to populate the dashboard in the same week, as soon as the month is over. 

### Are the numbers final upon release? Or will they be revised?

The numbers constructed in real time might not be final because the unemployment, vacancy, and labor force data are revised by the BLS after their initial release:

+ The number of job openings released by the BLS is preliminary and updated one month after its initial release, to incorporate additional survey responses received from businesses and government agencies and from the recalculation of seasonal factors. 
+ The BLS revises the prior five years of CPS and JOLTS data each year at the beginning of January, to account for revisions to seasonal factors, population estimates, and employment estimates. 

Yet, revisions to labor market data are generally minimal, especially compared to GDP revisions, so the information provided in real time by labor market data is [generally indistinguishable](https://perma.cc/W79A-EFPF) from the information provided in the final version.

### Is the unemployment rate the same as the BLS unemployment rate?

Yes, almost. The two unemployment rates are computed similarly, but the BLS [reports the unemployment rate](https://fred.stlouisfed.org/series/UNRATE) with one-digit precision, while we report it with two-digit (basis-point) precision. This higher precision is useful for recession detection, as recession indicators are computed and reported at the basis-point level.

### Is the vacancy rate the same as the BLS vacancy rate?

No. The BLS [computes the vacancy rate](https://fred.stlouisfed.org/series/JTSJOR) as the number of job vacancies divided by the number of employed workers plus job openings. This computation is problematic. First, it means that the BLS unemployment and vacancy rates are not consistent with each other, since one uses the number of employed workers plus unemployed workers in the denominator, while the other uses the number of employed workers plus job openings in the denominator. Second, the BLS vacancy rate is not a useful variable in labor market matching models.

By contrast, we compute the vacancy rate as the number of job vacancies divided by the number of employed workers plus unemployed workers. Our unemployment and vacancy rates are consistent with each other. Furthermore, our vacancy rate is a variable that appears directly in labor market matching models.

### Isn't the vacancy rate inflated by ghost job postings?

Vacancy data have recently been criticized for being polluted by ghost or fake vacancies. These vacancies do not actually represent an open position, and will not lead to a new hire. A [recent article by CBS News](https://perma.cc/JUR9-W4AA) explains that fake job listings are a growing problem in the labor market. [Employ America](https://perma.cc/XZ2B-LTNH) has gone one step further and argued that vacancy numbers are vacuous in general and should never used by policymakers. Let's go over the various criticisms raised by such pieces and address them.

###### Aren't vacancies poorly measured?

A first claim is that vacancy numbers are polluted by ghost vacancies. But vacancies are measured by the BLS, just like all other labor market statistics; they are not measured from online job postings. 

Specifically, the JOLTS asks firms to report the number of vacancies that they currently have, where a vacancy is defined as follows:

+ A specific position exists and work is available.
+ The job could start within 30 days.
+ The firm is actively recruiting workers from the outside to fill the position.

These questions are similar to the questions asked by the BLS to workers in the CPS in order to assess their labor force status. To be classified as a job seeker, a respondent must confirm that:

+ They do not currently  work but are willing to work.
+ They are available to start work immediately.
+ They have been actively searching for a job in the last four weeks. 

The threshold for reporting a vacancy is that same as the threshold for reporting being unemployed. The firm and the worker have to answer that they have been actively searching on the labor market—for instance through online job portals.

###### Isn't it exceedingly easy to post vacancies on online job boards?

A second point relates to online job boards: it is very easy for firms to list job advertisements online, so the number of online job postings might not be meaningful. As noted above, our vacancy numbers do not come from online job boards: they are measured by the BLS through JOLTS. So what happens on online job boards is irrelevant.

In fact, the internet and online job portals [do not seem to have much effect on the job market](https://doi.org/10.1257/000282804322970779). So there is no reason to believe that the job market is going to become fundamentally different because of online job portals. Looking at the academic job market, it does not seem that the amount of effort required to recruit colleagues is appreciably diminished by online job portals. Most of the recruiting time is spent on four things: reading applications and papers; interviewing candidates; flying out candidates; debating with colleagues. None of these four tasks are affected by online job boards.

###### Don't firms post more than one vacancy per hire?

A third supposed issue is that firms post more than one vacancy per hire—which leads some to believe that some vacancies are fake since they do not result in a hire. But this is exactly [how firms behave in matching models](https://youtu.be/45W3coPEObY)! In these models, if a firm wants to recruit one worker this month but knows that a vacancy is only filled with probability 1/3, then the firm will post 3 vacancies to hire one worker in expectation.

The key point is that in matching models, vacancies do not represent actual positions but recruiting effort—an effort to try to find workers through the matching process. This is also what vacancies represent in reality, as ZipRecruiter's Julia Pollak explains in the CBS article:

> When you have fewer candidates per opening, you have to be more creative. The high openings figure does partly reflect recruiting intensity, and not actual roles and seats and slots.

The bottom line is firms behave in reality exactly as in the model. The fact that firms post several vacancies per position does not mean that we should discount vacancy data. This behavior is what matching models predict.

###### Aren't vacancies just noise?

Another complaint is that vacancy numbers are just too noisy to be helpful. But, if vacancies were a vacant metric, we would expect them to be just noise. But vacancies and unemployment are [strongly negatively correlated](https://www.brookings.edu/interactive/historical-comparison-of-vacancy-and-unemployment-rates-and-full-employment-rate-of-unemployment-feru/?r=1788407&b=1), tracing a hyperbolic Beveridge curve. The Beveridge curve is [one of the most robust macro relationships](https://youtu.be/rA4S9lFiU3o)—how would it arise if vacancy data were vacuous? Given that unemployment and vacancies come from two entirely different sources—a firm survey, JOLTS, and a household survey, CPS—it is striking that they comove so closely.

###### Why are fake vacancies an issue now?

Firms have been posting vacancies for a century at least, so why do vacancies only appear fake now? The reason is that in 2022–2024, the labor market was exceptionally tight: the tightest it had been since the end of World War 2. Such exceptional tightness means that vacancies are filled at the slowest rate in the postwar period. Indeed, in a tight market, job seekers find jobs at a high rate, but [firms fill vacancies at a slow rate](https://youtu.be/t58mkFJ2Zlo)—as [predicted by matching models](https://youtu.be/TQ_fAN7rd6Q).

Because vacancies are filled at such slow rate, the number of vacancies posted for one actual position has exploded—reinforcing the impression of fake vacancies. But this was expected: this is exactly what matching models predict. Firms post several vacancies per position because they realize that the yield of each vacancy is low.

###### Conclusion

Although vacancies are not discussed much in the macro literature, there is an old and large literature that studies vacancies and explains how to measure them. In fact that literature is as old as the literature studying unemployment, going back to the work of [Beveridge in 1944](http://pinguet.free.fr/beveridge44.pdf), [Rees in 1957](http://www.nber.org/chapters/c2638), [Abraham in 1983](https://www.jstor.org/stable/1816568) and [in 1987](https://doi.org/10.2307/2534516), and [Zagorsky in 1998](https://doi.org/10.1162/003465398557438). Modern research on vacancies include work by [Barnichon in 2010](https://doi.org/10.1016/j.econlet.2010.08.029) and [Petrosky-Nadeau and Zhang in 2021](https://doi.org/10.1016/j.jmoneco.2020.01.009).

### What is full employment?

The federal government and Federal Reserve are mandated to maintain the economy at full employment, or maximum employment. (The two terms have been used interchangeably.). This legislative mandate comes from the [Employment Act of 1946](https://fraser.stlouisfed.org/title/1099), the [Federal Reserve Reform Act of 1977](https://fraser.stlouisfed.org/title/1040), and the [Full Employment and Balanced Growth Act of 1978](https://fraser.stlouisfed.org/title/1034) (known informally as the Humphrey–Hawkins Act).

The issue is that these texts do not explain what full employment is. The Humphrey-Hawkins Act did set an unemployment target of 3% within 5 years of the law (and 4% for young workers). [But these numbers were never taken seriously](https://www.jstor.org/stable/2138518), in part because policymakers rightly understood that the full-employment unemployment rate could not be a fixed number. When testifying in front of Congress in 1975 in his capacity of chair of the CEA, Alan Greenspan was asked what the target for full employment should be. [He responded:](https://doi.org/10.1177/003232927700700101)

> I do not think we should set a target.

But the Employment Act and Full Employment and Balanced Growth Act clearly state that achieving full employment is a way to maximize social welfare. So we translate full employment as social efficiency. Accordingly, we compute the FERU as the unemployment rate that achieves a socially efficient allocation of labor. This allocation maximizes social output by minimizing the uses of labor that are socially unproductive: both jobseeking and recruiting. The computation yields the formula $u^\ast = \sqrt{uv}$.

### Is the FERU the same as the NAIRU?

No. In recent times, the US government has used the non-accelerating-inflation rate of unemployment (NAIRU) as full-employment target. For instance, the [Joint Economic Committee recently wrote](https://perma.cc/E9V8-XTFH):

> Today, full employment is considered by many to be synonymous with the non-accelerating inflationary rate of unemployment (NAIRU)—the rate of unemployment that neither stokes nor slows inflation.

Similarly, in 2024, the [Council of Economic Advisers described](https://perma.cc/2JGM-QG4Z) the concept of full employment as follows: 

> Modern economics has generally defined full employment by citing the theoretical concept of the lowest unemployment rate consistent with stable inflation, which is referred to as $u^*$, the non-accelerating inflationary rate of unemployment (termed NAIRU).

These quotes are particularly meaningful because the Joint Economic Committee and Council of Economic Advisers were both created by the Employment Act of 1946 to ensure that the government achieved its full-employment mandate.

But this is a misconception: the NAIRU is an entirely different concept than the FERU. The FERU is the socially efficient unemployment rate. The NAIRU is the unemployment rate at which inflation remains stable. Since there is no guarantee that the unemployment rate prevailing under stable inflation is efficient, there is no guarantee that the NAIRU and FERU are the same.

### Is the FERU the same as the CBO's NRU?

Another full-employment target used by the US government is the natural rate of unemployment (NRU)—recently rebranded noncyclical rate of unemployment—constructed by the Congressional Budget Office (CBO). The [CBO's NRU is a slow-moving trend](https://perma.cc/NU5V-8ZY4) of the unemployment rate computed by assuming that the labor market was at full employment in 2005 and then incorporating changes in the demographic composition of the labor force over time. 

But, without a theory of full employment, it is impossible to know whether the US labor market really was at full employment in 2005, and by induction, whether the NRU in any year measures full employment. The NRU can therefore not be a satisfactory measure of full employment.

### Why is the FERU not constant?

The FERU is computed as the unemployment rate that maximizes social welfare, or equivalently that minimizes the nonproductive use of labor: both unemployment and recruiting. As it takes one worker to service one job vacancy, the nonproductive use of labor is measured by the number of job seekers and job vacancies. Through the Beveridge curve, the numbers of job seekers and vacancies are inversely related, so it is not possible to reduce the numbers of job seekers and job vacancies at the same time. Instead the social planner faces a tradeoff which is resolved by the FERU.

Because the FERU the describes the socially efficient position of the labor market on the Beverige curve, it is not constant but determined by the location of the Beverige curve. 
When the Beveridge curve shifts outward, the FERU increases; when the Beveridge cur shifts inward, the FERU decreases. Typical Beverige curve shifts do not affect the FERU much. For instance, between 1951 and 2019, the FERU remained between 3.1% and 5.5%, with an average value of 4.3%. The Beveridge curve did shift in and out during the postwar period, but the shifts were not large enough to produce noteworthy changes in the FERU. 

During the coronavirus pandemic, the Beveridge curve shifted out dramatically. The Beveridge curve then slowly shifted back inward. In 2025, the curve is almost back to its pre-pandemic position, although it remains somewhat further out. The dramatic shift raised the FERU signicantly: from 3.8% in January 2020 to 7.5% in April 2020. As the Beveridge curve normalized in the years after the pandemic, the FERU returned to normal levels. The FERU increase that followed the pandemic is extraordinary: such a large increase had never been recorded before. The pandemic was also the first time in the past century that the FERU crossed 6%.

---

## References

+ [u* = √uv: The Full-Employment Rate of Unemployment in the United States](https://pascalmichaillat.org/13/) (*Brookings Papers on Economic Activity*, 2024) – This paper obtains the formula for the FERU: $u^\ast = \sqrt{uv}$. The formula implies that the labor market is at full employment whenever there are as many job seekers as job vacancies ($u = v$); inefficiently tight when there are fewer job seekers than vacancies ($u < v$); and inefficiently slack when there are more job seekers than vacancies ($u > v$).

+ [Has the Recession Started?](https://pascalmichaillat.org/16/) (*Oxford Bulletin of Economics and Statistics*, 2025) – This paper develops the recession indicator and recession threshold, and computes the recession probability. The Michez rule, based on the recession indicator and threshold, detects recessions faster than the Sahm rule. It is also more robust in that it works between 1929 and 2024, whereas the Sahm rule breaks down before 1960.

## Raw data via FRED

+ [Number of job seekers, 1948–present](https://fred.stlouisfed.org/series/UNEMPLOY)
+ [Number of labor force participants, 1948–present](https://fred.stlouisfed.org/series/CLF16OV)
+ [Number of job openings, 2001–present](https://fred.stlouisfed.org/series/JTSJOL)

## BLS resources

+ [Latest CPS data release](https://www.bls.gov/news.release/empsit.nr0.htm)
+ [Latest JOLTS data release](https://www.bls.gov/news.release/jolts.nr0.htm)
+ [CPS homepage](https://www.bls.gov/cps/home.htm)
+ [CPS documentation](https://www.bls.gov/cps/documentation.htm)
+ [JOLTS homepage](https://www.bls.gov/jlt/)
+ [JOLTS documentation](https://www.bls.gov/jlt/jltfaq.htm)

---

{{< lastmod >}}

