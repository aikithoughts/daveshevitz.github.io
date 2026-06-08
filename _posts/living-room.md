---
title: "\"We can't paint the living room, we can't afford a plumber.\""
subtitle: "On scope creep, paralysis, and the value of incremental progress"
description: "On the paralysis of scope creep, and why it's okay to make incremental progress."
slug: living-room
date: 2026-04-09
---

<div class="story">
<p>Some time back, I was visiting a couple of friends of mine. They had just purchased a new house and were eager to show it off. We had a lovely dinner, then sat in their living room drinking coffee and chatting.</p>
<p>"I love your house," I said.</p>
<p>"Thanks!" they replied. "We do too. We just don't like the color they painted the living room."</p>
<p>"Well that's an easy fix," my wife replied. "Just take a weekend and repaint!"</p>
<p>"Oh. We can't paint the living room," they answered.</p>
<p>My wife and I looked at each other. "Why not?" I asked, finally.</p>
<p>"Because there are parts of the walls that need to be patched," they responded.</p>
<p>"Okay," I said. "That's just getting some putty or a little drywall repair. That shouldn't stop you from painting."</p>
<p>"Well, no," they admitted. "But if we're going to repair the drywall, we might as well move some electrical plugs around."</p>
<p>I thought for a moment. "Rewiring does make things a little harder," I said. "But not impossible. And probably something you can do if you want!"</p>
<p>"Yeah, but we can't do the electrical," they continued.</p>
<p>I looked at them. "And," I said carefully, "why can't you do the electrical?"</p>
<p>"Because!" they said. "If we're going to do the electrical, we should make some changes to the plumbing. And we just can't afford a plumber right now!"</p>
</div>

<p class="divider">* * *</p>

I think of this story frequently when I'm working on documentation. It's far too easy for me, sometimes, to think about the big picture. How will this solution scale? What is the long range impact of this decision? These are good questions to ask, for sure. But they also can prevent me from making progress.

I'll give an example. One project I worked on was the Angular JavaScript Framework. When I joined the team, the documentation had been left untended for a considerable period of time. As I was reading through the various topics, I saw all sorts of ways we could make the content easier to read and easier to discover.

But I also started falling into an issue similar to my friend's painting dilemma. If I was going to edit topics to remove passive voice, for example, then I should probably look at restructuring the topic to make the content easier to skim. And if I was going to restructure the content at a topic level, I should look at updating the information architecture across the board — and that's just a monumental undertaking!

Fortunately, I had a great mentor who reminded me that we didn't have to always get everything done all at once. So, I thought about the issue some more and decided on the following process:

1. Categorize the topics based on pageviews, which we used as a proxy for the popularity of the topic.
2. Ensure that, for every block of work, we were updating a few topics to improve the writing clarity.
3. If, to support a new feature, we needed to update a topic, we'd take the opportunity to improve the writing for the entire topic.
4. If, at any time, we had customer feedback about a topic that required immediate action, we'd improve the writing for the topic, as opposed to just fixing the bug.

This policy still meant that, sooner or later, we'd have to do other work to refactor and improve the docs, but we at least ensured incremental progress across the board.

And yes, I knew that this process meant that, later, we might end up completely gutting a section that we had just edited. But I figured the tradeoff was worth it. Better to have incremental progress that you occasionally have to undo, than to make no progress at all.

I still try to think big when it comes to documentation. But I also try to remind myself that it's okay to paint the living room even if I can't afford a plumber.
