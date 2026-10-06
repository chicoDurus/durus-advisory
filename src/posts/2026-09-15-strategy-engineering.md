---
title: Strategy That Can't Survive Contact With Engineering Isn't Strategy
slug: strategy-that-survives-engineering
date: 2026-09-15
cover: fracture
excerpt: A strategy that falls apart the moment engineers read it was a wish list. How to build strategy that holds up under technical scrutiny, and why engineering belongs in the room before the direction is fixed.
---

You have probably seen this happen. Leadership presents a new strategy. It's clear, ambitious and well argued. Then it reaches engineering, and within a week it starts to come apart.

The personalisation initiative needs data the platform doesn't collect. Entering three new markets in one quarter assumes a multi-currency setup that doesn't exist. A single customer account across all brands would mean rebuilding an authentication layer that six other systems depend on.

Nobody was careless. The strategy was built in good faith, just without the people who know what the platform can actually do.

## Why it keeps happening

Strategy is usually built at the top: leadership offsites, commercial planning, board conversations. Engineering leadership may be present, but often as an audience rather than a co-author.

Technical constraints are invisible from outside. To a commercial lead, "add another currency" sounds like a settings change. To the engineer who built the payment layer, it might be four months of work and a data migration.

Feasibility gets treated as a later step. The direction is agreed first and handed to engineering to work out how. By the time the constraints surface, people are invested in the plan and reluctant to change it.

And engineers learn to keep quiet. If raising concerns gets labelled as negativity, people stop raising them. The problems don't go away. They come back later, as delays.

## What a durable strategy looks like

It's grounded in the platform as it is today, including its debt and the real capacity of the teams.

It names the enabling work. If a commercial goal depends on a platform change, that change is part of the strategy, with time and people allocated, instead of something engineering is expected to squeeze in.

It separates goals from solutions. "Increase cross-brand retention" is a goal. "Build a unified customer account" is one way to get there. Keeping them apart lets engineering propose a cheaper route to the same result.

It's honest about cost. If the platform team spends the first half of the year on infrastructure, new features will slow down. A good strategy says so openly.

## How to build it

Bring a senior engineer or architect into the strategy conversation before the direction is fixed. They're there to flag the expensive assumptions while those are still cheap to change. Engineers can build almost anything given enough time, so "can we do this?" is the wrong question. "What would this take, and what's the simplest version that gets most of the value?" is the right one.

Run a short feasibility check on every major bet. A week or two is usually enough to know whether you're planning a three-week project or a nine-month one, what it depends on, and which technical assumption is riskiest.

Invest in the platform on purpose. On multi-brand and multi-market platforms especially, a shared component library, a configurable market layer or a clean data model can turn future launches from projects into configuration. If the strategy never includes platform investment, every new initiative pays for the shortcuts taken on the last one.

Keep the loop open. Schedule regular points where engineering reports what it has learned, whether that's "this is harder than we thought" or "we found a much simpler way". Both should be able to change the plan.

Treat pushback as information. When an engineer says something won't work as planned, ask what the constraint is and what it would take to remove it. Teams that are allowed to push back surface problems early. Teams that aren't surface them late, when they cost more.

## A simple test

Hand your current strategy to your most experienced engineer and ask for the three assumptions most likely to break it. If they find serious ones in an afternoon, the strategy isn't ready.

That's a good outcome. It's exactly the moment you want to find out, before the roadmap is built, before commitments are made to the board, and before the quarter is half gone.
