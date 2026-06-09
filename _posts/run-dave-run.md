---
title: "Run, Dave, Run!"
subtitle: "On falling down, getting up, and shipping anyway."
description: "Writing single-use apps in the age of AI"
slug: run-dave-run
date: 2026-05-29
---

A couple of years ago, I was running the Ragnar Relay: Northwest Passage. This is a 200-ish mile relay race that starts up in Blaine, WA and finishes in Langley, WA. The standard Ragnar Road Relay consists of a team of 12 runners, split into two vans. The total distance is split between all 12 runners, with each runner running 3 legs. It's a fun time, made all the more so when you have a great group of people to run with, which I did.

I was just starting my second leg, which was about 6 miles long. It was the worst time of day for me to see — twilight. I started my leg, made it about a quarter of the mile, and totally tripped on the sidewalk. Skinned up my leg and forearm something fierce. I had decided (stupidly) to NOT wear my glasses, and I couldn't see my phone, so I could barely text my team: "Fell down." Which, of course, made them panic until they eventually found me. (I was mostly fine, and finished the race without issue.)

That was a few years ago, and now I'm facing my first ultramarathon in about 2 weeks. This is a 62 mile run and is by far the longest distance I've ever run. I'm excited, but I know the risks. And I thought: I'll have my phone, but it would be great to have a way to communicate with my support crew if I need to. Something easy, like a set of buttons that shared if I was doing well, needed water, or (worst case), needed help.

Tonight, I decided to build that app myself. The app is, understandably, called "Run, Dave, Run!" You can check it out at [rundaverun.daveshevitz.com](https://rundaverun.daveshevitz.com), and the code is all open source at [github.com/aikithoughts/rundaverun](https://github.com/aikithoughts/rundaverun). The stack is Next.js with TypeScript, MongoDB for storing check-ins and status updates, Leaflet for the map, and Vercel for hosting. TypeScript is somewhat new to me. I know JavaScript pretty well, but TypeScript's type system is something I've been meaning to get more comfortable with. This felt like a good excuse.

The app works pretty simply. The main page is a supporter view where folks can watch my progress on a live map. For me, there's a runner's page that requires a PIN to access. When I'm on the runner page, I can tap to check in at named checkpoints along the course, and I can tap a status button to let anyone tracking me know what's going on — or, if things go sideways, hit the SOS button.

Now, I admit I'm not a professional developer. In my career as a content strategist and developer documentation writer, I have written a lot of code. But most of that code has been examples or snippets. Rarely have I needed to create a full-fledged app. Nonetheless, I know enough about app development that, when building RunDaveRun, I found myself thinking:

- What should I do about authentication and authorization?
- How should I handle errors?
- What sort of testing framework should I use?
- How should I support multiple races? Multiple users?

Basically, how do I build a professional, shippable app?

These questions have, in the past, often led me to just...not code. It's too much work for something that I may not use that much anyway.  But with AI, I don't have to make that choice. I can build RunDaveRun for me. Not only that, I can build it for one race. After my 100k, I don't ever have to use it again if I don't want to.

When I had that realization, the app suddenly didn't seem so hard to build. So I let AI do its work, building out a perfectly functional, perfectly NOT scalable application. And it works! Or, perhaps more accurately, it works well enough for what I need it to do this weekend.

I think the real change here isn't that AI helped me code faster. It's that it changed how I thought about whether to build this at all. Questions about authentication, error handling, testing, and scalability are the right questions if you're building something for a lot of people. I wasn't. I was building something for me. Something I would use for one race and then maybe never again. Before, that kind of project just felt like too much work.

I think AI is opening the door for a new type of app: the single use app. These are apps that you build once, for a particular reason, and then never use again. Building apps like this means you don't have to worry about a whole host of issues, but you do get the benefit that only a software application can provide. In addition, you get more control over your app experience and, perhaps even more importantly, your data. You don't have to care about performance, scalable architectures, or any of those things. Better still, you can always change your mind later. I might decide to use this app again. If I do, it's trivial to hardcode a new race. I wonder how many times I'll do that before I finally decide I want to build something more robust? That day might never come.

We don't have to build for production any more, if we don't need to. We can just build for ourselves.