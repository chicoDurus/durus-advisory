---
title: "Agile, Scrum, Waterfall, Kanban: What's Actually Different"
slug: agile-scrum-waterfall-kanban
date: 2026-05-26
cover: frameworks
excerpt: People use these words as if they were interchangeable. They aren't. A plain-language guide to the main delivery frameworks, what each assumes about your work, and when each one fits.
---

In most organisations I've worked with, "agile" means "we do standups" and "waterfall" means "the old way, before we got better". Both are wrong, and the confusion causes real problems. Teams pick a framework because it's fashionable, not because it fits the shape of their work.

So here's a plain-language map of the main options and what each one actually assumes.

## Agile is a philosophy, not a process

Start here, because it's the most misused word of the lot.

Agile comes from the 2001 Agile Manifesto: four values and twelve principles written by a group of software practitioners. The core idea is simple. Build in small increments, get feedback early, and adapt the plan as you learn, instead of trying to specify everything up front.

Agile doesn't tell you how long a sprint is, what meetings to hold or what roles you need. It's a set of priorities. Scrum, Kanban, XP and others are frameworks that try to put those priorities into practice.

When someone says "we're agile", the useful follow-up is: which practices, and why?

## Waterfall: sequence first

Waterfall runs work through fixed phases in order: requirements, design, build, test, release. Each phase finishes before the next starts, and changes late in the process are expensive.

It gets a bad reputation, and in software it's often deserved. Requirements change, users surprise you, and finding out in month nine that you built the wrong thing is painful.

But waterfall assumes something that is sometimes true: that the requirements are known, stable and costly to get wrong. Some examples:

- A regulatory change with a fixed deadline and a precise specification
- An integration against a third-party API that won't change
- Hardware, infrastructure or migration work where you can't iterate in production

In those cases, careful upfront planning isn't bureaucracy. It's risk management.

## Scrum: fixed rhythm, fixed roles

Scrum is the most popular agile framework, and it's quite specific. Work happens in sprints, usually one or two weeks long. There are three roles (product owner, scrum master, developers) and a set of events (sprint planning, daily scrum, sprint review, retrospective).

What Scrum assumes:

- The work can be broken into pieces that deliver value within a sprint
- Priorities can be held steady for the length of a sprint
- The team is stable and cross-functional enough to finish work without constant hand-offs

When those assumptions hold, Scrum is excellent. It creates a predictable rhythm, forces regular prioritisation and builds in feedback.

When they don't hold, it gets uncomfortable. A team that handles a lot of urgent, unplanned work (production incidents, compliance requests, operator escalations) will find its sprint plan blown apart every few days.

## Kanban: flow over cadence

Kanban comes from manufacturing. Instead of planning in fixed time boxes, you visualise work on a board, limit how much can be in progress at once, and pull new work in when capacity frees up.

There are no prescribed roles or sprints. The key practices are:

- **Visualise the workflow** so everyone sees where work is and where it's stuck
- **Limit work in progress** so the team finishes things instead of starting them
- **Measure flow** using cycle time and throughput, and improve from there

Kanban suits teams with a continuous, unpredictable stream of work: platform teams, support engineering, content operations, data requests. It's also a good starting point for teams that need more structure but aren't ready to take on Scrum's full set of events.

## The rest of the family

A few other names you'll hear:

- **Scrumban** combines Scrum's planning and retrospectives with Kanban's flow and WIP limits. Very common in practice, even when teams don't call it that.
- **Extreme Programming (XP)** focuses on engineering practices: pair programming, test-driven development, continuous integration. It pairs well with Scrum or Kanban rather than replacing them.
- **SAFe, LeSS and Nexus** are scaling frameworks that coordinate many agile teams working on one product. They add structure (and overhead) to handle cross-team planning and dependencies.
- **Shape Up**, from Basecamp, uses six-week cycles with fixed time and variable scope, followed by a cooldown. It suits small product teams that want fewer meetings and more autonomy.

## A quick comparison

| | Waterfall | Scrum | Kanban |
|---|---|---|---|
| Planning | Up front, in full | Every sprint | Continuous |
| Change | Expensive | Between sprints | Any time |
| Roles | Project manager, phase owners | PO, scrum master, developers | None prescribed |
| Measures | Milestones, budget | Velocity, sprint goals | Cycle time, throughput |
| Best for | Stable, well-specified work | Product development with a steady team | Continuous or unpredictable work |

## How to choose

Don't start with the framework. Start with three questions about your work.

**How predictable is it?** If most work is planned and priorities hold for a couple of weeks, Scrum fits. If a large share arrives unplanned, Kanban will cause less pain.

**How well do you understand the requirements?** If they're fixed and the cost of mistakes is high, more upfront design is sensible, whatever you call it. If you're exploring, short iterations win.

**How many teams are involved?** One team can run almost anything. Five teams on one platform need a way to coordinate dependencies, and no team-level framework provides that on its own.

Most mature teams end up with a hybrid. Sprints for product work, a Kanban lane for operational requests, and a bit of upfront specification for regulatory or integration projects. That's not a failure of discipline. It's matching the process to the work.

The framework is a tool. If your team spends more time debating whether it's "doing Scrum properly" than shipping things users care about, the tool has become the job.
