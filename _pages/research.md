---
permalink: /research/
title: "Research/Tools"
---

My research is interdisciplinary, encompassing social media/computational social science, web/data science, web archiving, and (local) news.

## StoryGraph

[StoryGraph](https://web.archive.org/storygraph/) provides a collection of tools that analyze the news cycle. [USA](https://web.archive.org/storygraph/graphs/usa/) generates a news similarity graph every 10 minutes by computing the similarity of news stories from 17 US news sources across the partisanship spectrum (left, center, and right). In these graphs, the nodes represent news articles, and an edge between a pair of nodes represents a high degree of similarity between the nodes (similar news stories).

<table align="center" style="border: 1px solid white; border-collapse: collapse;">
  <tr>
    <td style="border: 1px solid white; border-collapse: collapse;">
      <a href="https://web.archive.org/storygraph/graphs/usa/#cursor=98&hist=1440&t=2019-03-21T16:26:25" target="_blank" title="Click me :) Slow news cycle story graph">
        <img src="/images/research/sample_graph_1.png" alt="Slow news cycle story graph" class="img">
      </a>
    </td>
    <td style="border: 1px solid white; border-collapse: collapse;">
      <a href="https://web.archive.org/storygraph/graphs/usa/#cursor=115&hist=1440&t=2019-11-17T19:15:38" target="_blank" title="Click me :) Split attention story graph">
        <img src="/images/research/sample_graph_2.png" alt="Split attention story graph" class="img">
      </a>
    </td>
    <td style="border: 1px solid white; border-collapse: collapse;">
      <a href="https://web.archive.org/storygraph/graphs/usa/#cursor=135&hist=1440&t=2019-03-24T22:32:21" target="_blank" title="Click me :) Mueller report story graph">
        <img src="/images/research/sample_graph_3.png" alt="Mueller report story graph" class="img">
      </a>
    </td>
  </tr>
  <caption align="bottom">Three news similarity graphs illustrating the dynamics of the news cycle. In these graphs, a single node represents a news article, a connected component (multiple connected nodes) represents a single news story reported by the connected nodes. StoryGraph uses the average degree of the connected components to quantify the level of attention stories receive. <a href="https://web.archive.org/storygraph/graphs/usa/#cursor=98&hist=1440&t=2019-03-21T16:26:25" target="_blank">The first graph</a> shows what is often referred to as a slow news day; low overlap across different news media organizations. <a href="https://web.archive.org/storygraph/graphs/usa/#cursor=115&hist=1440&t=2019-11-17T19:15:38" target="_blank">The second graph</a> shows a scenario where the attention of the media is split across multiple news stories. <a href="https://web.archive.org/storygraph/graphs/usa/#cursor=135&hist=1440&t=2019-03-24T22:32:21">The third graph</a>, which is about the release of the [Mueller Report](https://en.wikipedia.org/wiki/Mueller_report), shows a major news event; high degree of overlap/connectivity across different news media organizations.</caption>
</table>

## StoryGraphBot

[StoryGraphBot](https://twitter.com/storygraphbot) is a Twitter bot that runs every hour, tracking top news stories and creating tweet threads that report updates (rising/falling/same attention) of the stories. See also, <a href="https://ws-dl.blogspot.com/2021/05/2021-05-10-chronicling-life-cycle-of.html" target="_blank">Chronicling the life-cycle of top new stories with StoryGraphBot</a>.

<figure>
  <a href="https://web.archive.org/storygraph/graphs/usa/#cursor=135&hist=1440&t=2019-03-24T22:32:21" target="_blank" title="Story Attention Dynamics Graph">
    <img src="/images/research/sgbot_tracking_stories.png" alt="Story Attention Dynamics Graph" class="img">
  </a>
  <figcaption>
    Story Attention Dynamics chart illustrating the life-cycle of two top news stories from May 18, 2018 -- May 19, 2018. Each line (red or blue) represents a top news story. The x-axis represents time while the y-axis represents the average degree of Connected Components (representation of story). Within our window of observation, the <a href="https://twitter.com/storygraphbot/status/1388942915574112264" target="_blank">Santa Fe High School Shooting</a> story received peak attention on Friday May 18, 2018 at 4:40PM, this attention waned with the lowest point coinciding with the rise of a new story, the <a href="https://twitter.com/storygraphbot/status/1388943136127393796" target="_blank">Royal Wedding of Prince Harry and Meghan Markle</a>.
  </figcaption>
</figure>

## Local Memory Project

[Local Memory Project](http://www.localmemory.org/) helps users and small communities discover, collect, build, archive, and share collections of stories for important local events from local sources.

<table align="center" style="border: 1px solid white; border-collapse: collapse;">
  <tr>
    <td style="border: 1px solid white; border-collapse: collapse;">
      <a href="https://web.archive.org/storygraph/graphs/usa/#cursor=98&hist=1440&t=2019-03-21T16:26:25" target="_blank" title="Click me! Slow news cycle story graph">
        <img src="/images/research/LMG0.png" alt="Slow news cycle story graph" class="img">
      </a>
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid white; border-collapse: collapse;">
      <a href="https://web.archive.org/storygraph/graphs/usa/#cursor=115&hist=1440&t=2019-11-17T19:15:38" target="_blank" title="Click me! Split attention story graph">
        <img src="/images/research/LMG1.png" alt="Split attention story graph" class="img">
      </a>
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid white; border-collapse: collapse;">
      <a href="https://web.archive.org/storygraph/graphs/usa/#cursor=135&hist=1440&t=2019-03-24T22:32:21" target="_blank" title="Click me! Mueller report story graph">
        <img src="/images/research/LMG2.png" alt="Mueller report story graph" class="img">
      </a>
    </td>
  </tr>
  <tr>
    <td style="border: 1px solid white; border-collapse: collapse;">
      <a href="https://web.archive.org/storygraph/graphs/usa/#cursor=135&hist=1440&t=2019-03-24T22:32:21" target="_blank" title="Click me! Mueller report story graph">
        <img src="/images/research/LMG3.png" alt="Mueller report story graph" class="img">
      </a>
    </td>
  </tr>
</table>

## Sumgram

<a href="https://github.com/oduwsdl/sumgram/">Sumgram</a> is a Python tool that summarizes text collections with their most frequent conjoined n-grams. See also, <a href="https://ws-dl.blogspot.com/2019/09/2019-09-09-introducing-sumgram-tool-for.html" target="_blank">Introducing sumgram, a tool for generating the most frequent conjoined ngrams.</a>

<figure>
  <a href="https://github.com/oduwsdl/sumgram" target="_blank" title="Sumgrams vs. ngrams">
    <img src="/images/research/sumgrams_ebola.png" alt="Sumgrams vs. ngrams" class="img">
  </a>
  <figcaption>
    Comparison of top 20 (first column) bigrams, top 20 (second column) six-grams, and top 20 (third column) sumgrams (conjoined ngrams) generated by sumgram for a collection of documents about the <a href="https://en.wikipedia.org/wiki/Western_African_Ebola_virus_epidemic" target="_blank" title="Sumgrams vs. ngrams">2014 Ebola Virus Outbreak</a>. Proper nouns of more than two words (e.g., "centers for disease control and prevention") are split when generating bigrams, sumgram strives to remedy this. Generating six-grams surfaces non-salient six-
  </figcaption>
</figure>

## What Did It Look Like

<a href="https://whatdiditlooklike.mementoweb.org/">What Did It Look Like</a> is a Twitter bot that replies to a tweet that contains the <a href="https://twitter.com/search?q=%23whatdiditlooklike&src=hashtag_click">#whatdiditlooklike</a> hashtag and a URL, with a Tumblr post of the yearly snapshot of what the webpage looked like.

<div class="tumblr-post" data-href="https://embed.tumblr.com/embed/post/BorIHM7tNBoluohrX2jGVA/95919248149" data-did="63d92e4d7a4129686a7480c86692fcf4aa033c7f"><a href="https://whatdiditlooklike.mementoweb.org/post/95919248149/what-did-http-www-facebook-com-look-like">https://whatdiditlooklike.mementoweb.org/post/95919248149/what-did-http-www-facebook-com-look-like</a></div>  <script async src="https://assets.tumblr.com/post.js"></script>
