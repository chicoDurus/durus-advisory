---
title: Strategy That Can't Survive Contact With Engineering Isn't Strategy
slug: strategy-that-survives-engineering
date: 2026-09-15
cover: fracture
excerpt: A strategy that falls apart the moment engineers look at it was a wish list with a nice cover. How to build strategy that holds up under technical scrutiny, and why engineering belongs in the room early.
---

There's a moment in many product organisations that everyone recognises. Leadership presents the new strategy. It's clear, ambitious and well argued. Then it reaches the engineering team, and within a week it has fallen apart.

The new personalisation engine needs data the platform doesn't collect. The plan to launch three markets in one quarter assumes a multi-currency wallet that doesn't exist. The single unified player account across brands would require rebuilding the authentication layer that six other systems depend on.

Nobody was being careless. The strategy was built in good faith. It was just built without the people who understand what the platform can actually do.

## Why this keeps happening

**Strategy is usually built at the top.** Leadership, commercial and product leads work out direction in workshops and offsites. Engineering leadership might be present, but often as a listener, not a co-author.

**Technical constraints are invisible from the outside.** To a commercial stakeholder, "add another currency" sounds like a configuration change. To the engineer who knows how the wallet was built, it might be four months of work and a data migration.

**Feasibility is treated as a later step.** The strategy is agreed first, then handed to engineering to "work out how". By the time constraints surface, people are invested in the plan and reluctant to change it.

**Engineers learn not to push back.** If raising concerns gets labelled as negativity, people stop raising them. The problems still exist. They just come out later, as delays.

## What a durable strategy looks like

A strategy that survives engineering scrutiny has a few characteristics.

**It's grounded in the platform as it is.** It acknowledges the current architecture, the technical debt and the real capacity of the teams. It doesn't assume capabilities that don't exist without planning to build them.

**It names the enabling work.** If the commercial goal depends on a platform change, the platform change is part of the strategy, with time and people allocated to it. It's not something engineering is expected to fit in around the edges.

**It separates goals from solutions.** "Increase cross-brand retention" is a goal. "Build a unified player account" is one possible solution. Keeping these separate lets engineering propose a cheaper route to the same outcome.

**It makes the trade-offs explicit.** Every strategic choice costs something. If the platform team spends the first half of the year on infrastructure, new features will slow down. A good strategy says so openly instead of pretending both can happen at full speed.

## How to build it

### Bring engineering in before the direction is fixed

Not to approve the plan, but to help shape it. A senior engineer or architect in the strategy conversation from the start will flag the expensive assumptions while they're still cheap to change.

The question to ask isn't "can we do this?" Engineers can do almost anything given enough time. The better question is: "What would this take, and what's the simplest version that gets us most of the value?"

### Run a feasibility pass on the big bets

For each major strategic initiative, spend a week or two on a lightweight technical assessment before committing:

- What does the current platform support?
- What needs to change, and how big is that change?
- What are the dependencies on other systems, vendors or teams?
- What's the riskiest technical assumption, and how could we test it cheaply?

This isn't a full design. It's enough to know whether you're planning a three-week project or a nine-month one.

### Invest in the platform deliberately

In multi-brand and multi-market environments especially, the platform is what makes the commercial strategy possible. A shared component library, a configurable market layer or a clean data model can turn future launches from projects into configuration.

If the strategy never includes platform investment, every new initiative pays the cost of the shortcuts taken last time.

### Keep a feedback loop open

Strategy shouldn't be a one-way handover. Schedule regular checkpoints where engineering can report what they've learned. Sometimes that's "this is harder than we thought". Sometimes it's "we found a much simpler approach". Both should be able to change the plan.

### Treat pushback as information

When an engineer says something won't work as planned, the useful response is curiosity, not frustration. What's the constraint? What would it take to remove it? Is there another way to reach the same goal?

Teams where pushback is welcomed surface problems early. Teams where it's punished surface them late, when they cost more.

## The product owner's role

This is where good product leadership earns its keep. The product owner sits between the commercial ambition and the technical reality, and the job is to make the two meet.

That means understanding the platform well enough to spot unrealistic assumptions, translating constraints into commercial terms leadership can act on ("we can launch two markets this quarter, or three if we delay the loyalty feature"), and protecting time for the enabling work that never looks exciting on a slide.

## The test

A simple way to check your current strategy: give it to your most experienced engineer and ask them to find the three assumptions most likely to break it. If they find serious ones in an afternoon, the strategy isn't ready.

That isn't a failure. It's exactly the moment you want to find out, before the roadmap is built, before commitments are made and before the quarter is half gone. A strategy that has already survived that conversation is one you can actually deliver.
