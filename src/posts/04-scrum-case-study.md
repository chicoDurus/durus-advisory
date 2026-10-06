---
title: "Bringing Scrum Into a Disorganized Organization: A Case Study"
slug: scrum-in-a-disorganized-organization
date: 2026-06-23
cover: chaos
excerpt: No backlog, five people setting priorities, and releases that slipped by default. How one product team moved from chaos to a working rhythm in a quarter, and what I'd do differently.
---

*This is a composite case drawn from more than one engagement. Company details are removed and figures are rounded, but the problems and the sequence of fixes are real.*

## The starting point

The company ran a set of consumer-facing web products on a shared platform. About twelve engineers, two QA, one designer and a product function that was really one overloaded person. Revenue was healthy, which is partly why the problems had been tolerated for so long.

When I arrived, a few things were obvious within the first week.

**There was no single backlog.** Work lived in Jira, in a shared spreadsheet owned by marketing, in Slack threads and in the CEO's notes. Engineers picked up whatever the last person to message them asked for.

**Five people set priorities.** The CEO, the head of marketing, the head of operations, the compliance lead and the CTO could all put work into the team, and all of them did. Nobody could say no, so everything was "urgent".

**Nothing finished.** At any given time the team had more than forty tickets in progress. Cycle time for an ordinary feature was measured in months. Releases happened when someone decided enough had piled up.

**Everyone was busy and nobody was happy.** Engineers felt pulled in all directions. Stakeholders felt ignored. Leadership felt the team was slow and wondered whether it needed more people.

## Week 1–2: Make the work visible

I didn't start with Scrum. I started with a list.

Every piece of work, from every source, went into one Jira project. That took most of the first week and surfaced about 280 items. Roughly a third were duplicates, already done or no longer relevant. We closed them.

Then we put up a simple board with five columns: To do, In progress, In review, Testing, Done. Everything currently being worked on went into In progress. Seeing forty-plus cards in that column did more to convince leadership than any presentation I could have given.

**Lesson:** you can't fix a process people can't see. Visibility comes first, and it's often enough to start the right conversations on its own.

## Week 3–4: One owner for priorities

This was the hardest step, and it wasn't a process change. It was a leadership decision.

I put a proposal to the CEO: one product owner owns the order of the backlog. Everyone else can request, argue and escalate, but the order is decided in one place. Requests go through a weekly prioritisation session where stakeholders can make their case.

It took two meetings to agree. The concern was that the product owner would become a bottleneck. What changed the CEO's mind was a simple exercise. We listed the top ten "urgent" items from each stakeholder and asked which ones he would do first. He couldn't answer without a conversation, which was exactly the point.

We also created an explicit fast lane for genuine emergencies: production incidents and regulatory deadlines. Everything else went through the weekly session.

**Lesson:** Scrum assumes a product owner with real authority. If the organisation won't grant it, no amount of ceremony will compensate.

## Week 5–6: Limit work in progress

With one ordered backlog, we set a hard limit: no more than eight items in progress across the team. New work couldn't start until something finished.

The first two weeks were painful. Engineers had to swarm on stuck items, testers became a visible bottleneck, and code reviews that had sat for weeks suddenly mattered. But cycle time started dropping almost immediately, and for the first time in months things were actually reaching Done.

## Week 7 onward: Introduce the Scrum rhythm

Only now did we introduce sprints. Two weeks, with:

- **Sprint planning**, capped at 90 minutes, with a single sprint goal
- **A 15-minute daily scrum** focused on the board, not status reports
- **A sprint review** where stakeholders saw working software
- **A retrospective** with one agreed improvement each time

We kept the emergency lane and reserved about 20% of capacity for it, based on what the previous month's unplanned work had actually been. When the lane wasn't used, the team pulled from the backlog.

The sprint review turned out to be the most valuable event by far. Stakeholders who had felt ignored for a year now saw progress every two weeks, and they could change direction based on something real rather than a ticket description.

## Results after one quarter

Rounded, and measured against the month before we started:

- Work in progress went from 40+ items to under 10
- Median cycle time for a standard feature dropped from around ten weeks to under three
- Releases moved from irregular batches to a predictable two-week rhythm
- Unplanned work stabilised at around 20% of capacity, and it was now visible and accounted for

The less measurable result mattered more. Arguments about priority moved from Slack DMs into a single weekly meeting. Engineers stopped feeling like they were serving five masters.

## What I'd do differently

**I'd involve QA in the redesign earlier.** Limiting WIP immediately exposed testing as the bottleneck, and the QA engineers felt blamed for a problem the old process had hidden. We fixed it by pairing developers with testers and automating the most repetitive regression checks, but I should have seen it coming.

**I'd set the definition of done on day one.** For the first few sprints, "done" meant different things to different people. Some meant merged, some meant deployed, some meant tested in production. A short, written definition would have saved several awkward reviews.

**I'd spend less time on velocity.** Leadership wanted a number, and velocity became that number. It took effort to shift the conversation to cycle time and sprint-goal completion, which said much more about how well the team was delivering.

## The takeaway

The team didn't need Scrum first. It needed visibility, a single owner for priorities and a limit on how much it tried to do at once. Scrum gave that a rhythm, but the rhythm only worked because the foundations were already in place.

If you're about to introduce Scrum into an organisation that feels chaotic, resist the urge to roll out all the ceremonies on day one. Fix ownership and visibility first. The framework sticks much better on a foundation that already makes sense to people.
