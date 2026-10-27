---
title: "Everything in Software Is Amazing and Nobody's Happy"
date: 2020-03-20
series: other
author: Eugene Trifonov
cover: ../images/software2020/01.jpg
teaser: "There's a typical position you can come across on Habr and beyond: \"even though hardware keeps getting better over the years, humanity has cancelled out the effect by writing ever worse software\"."
translation: machine
---

![](../images/software2020/01.jpg)

There's a typical position you can come across on Habr (a Russian tech site) and beyond: "even though hardware keeps getting better over the years, humanity has cancelled out the effect by writing ever worse software".

As in: processors have more cores now, but everything lags more than ever. Electron and Slack are spawns of darkness, sent to rob us of happiness and memory. Mobile apps have become hungrier than old operating systems. And operating systems themselves no longer make any real progress, yet for some reason they keep bloating. How much better it was back when people could fit an OS on a floppy disk!

I'll say it plainly: when I see statements like that, it drives me up the wall. I think they miss a whole range of important factors. And in the end the situation resembles Louis C.K.'s classic bit «[Everything's amazing and nobody's happy](https://www.youtube.com/watch?v=MkS3hyzarrA)»: everything has become amazingly good, and people sit around complaining.

So I decided to describe these missing factors. Since the text came out sharp, I want to stress that the opinion is entirely my own (even though I refer to the conferences of the company I work for).

## Selective memory

There's a well-known nostalgia effect: "the grass was greener and the music was better back then". But I think for many people this effect takes on frightening proportions, when their feelings diverge dramatically from reality.

I'm talking about statements like this one: "Almost everything on computers feels slower than in 1983". Judging by the thousands of likes, this isn't an isolated opinion but a widespread one.

> almost everything on computers is perceptually slower than it was in 1983
>
> — Gravis (edited) (@gravislizard) [November 6, 2017](https://twitter.com/gravislizard/status/927593460642615296)

My first reaction: "And how did streaming 4K video feel in 1983?" That is, let's start by remembering that most of today's uses of a computer were impossible back then, partly precisely because of speed. Once upon a time a film (not even in 4K, but in 1080p) would have taken months to download, and then the computer couldn't have played it at 24 FPS. So how do you compare today's speed with a speed so unimaginably low that it didn't exist at all?

Second reaction: yes, some things that moved from the command line to a GUI may take longer there. I'm willing to believe that Word in 2020 starts slower than the console editor vi did in 1983 (I can't compare personally: I first sat at a computer in the 90s). But if this matters so much to you, you can still use the command line for many "tasks from the 80s" in 2020. I'm writing this text in vim right now: a wonderful editor that keeps up with the times thanks to its plugin ecosystem. It looks great on a modern Retina iMac: the letters have become very crisp, and it still responds instantly. So what's the problem?

But the main point isn't even these two things. What matters more is this: I think we've started to forget how slow computers used to be. When something starts to lag more, we notice it immediately, but when something becomes faster or easier, we simply take it for granted and forget the past.

To everyone who writes "everything used to be faster", I have this question: do you even remember, say, this?

![](../images/software2020/02.png)

I'll be honest: I don't really think about it myself either. When I shut down my computer today, I don't reflect on how twenty years ago I sat and waited between pressing a button in the OS and pressing the button on the system unit. I simply took it for granted that this is no longer necessary and forgot that it was ever otherwise.

Startup times have changed a lot too. Now I sit down at my iMac, press one key, and a second later it's ready to work (thanks to SSDs and sleep mode). As a kid waiting for Windows to boot from an HDD, I would hardly have believed I'd live to see this.

"When an email has a gazillion images, it opens terribly slowly, sometimes as long as ten seconds!" I understand that can be annoying, but listen: in 2000, to check my email I first spent a minute enjoying the trills of the modem, then waited for the webmail's main page to load at its leisure, and then the email itself didn't load instantly either, and it had no images at all, only text. Today something like that would open without delay. Maybe we just shouldn't stuff a thousand images into a means of communication that was invented for something else? And before declaring "everything has gone downhill", let's think: how long would an email with that many images have taken to open in 2000?

Or here's another memory, lost in time, like tears in rain. In the 2000s there was a popular joke: "A slow computer is when you know all the Photoshop developers by name." For those who don't get it: back then, pirated Photoshop was very popular in Russia, and every time they launched it, Russians had to stare at this for a long time:

![Oh, I just realized I know one of these people: Sean Parent gave a talk at our C++ Russia conference](../images/software2020/03.png)
*Oh, I just realized I know one of these people: Sean Parent [gave a talk](https://www.youtube.com/watch?v=Xtk_JXDqmxo) at our C++ Russia conference*

Now compare. Today people joke: "Once it took two kilobytes of memory to put a man on the Moon, and now it takes two gigabytes to run Slack." It sounds punchy, but do you notice the difference? However much RAM Slack consumes, users don't face the situation of "you can go make tea while the program starts". Everything has gotten better, and we didn't notice.

Or here's a telling historical artifact: the 2002 episode «Даунлоад» ("Download") of «Масяня», a hugely popular Russian Flash cartoon series. The characters are terribly worried about a disconnect that would force them to download a file all over again.

https://www.youtube.com/watch?v=m05xKxkIGU4

Note: the file they're downloading is 591 kilobytes. The characters are worried about having to re-download half a megabyte. That was the real state of things in 2002.

For comparison, a recent example from my own life. I had a small technical problem on my Mac, and on Stack Overflow I found the advice "install Xcode and accept its terms of use". My reaction: it's odd to download an 8-gigabyte IDE to press one button, but if it helps, why not.

So program sizes have grown over the years (in the days of «Масяня», an "8-gigabyte IDE" would have made people's hair stand on end), but downloading them has become much easier, and our lives have become much better.

And the last example in this section is about "bloated mobile apps". Every now and then people write indignant posts like «[App sizes are out of control](https://trevore.com/post/app-sizes-are-out-of-control/)»: since when does LinkedIn take up 275 megabytes on a phone?! In 2018 you could [read](https://tonsky.me/blog/disenchantment/) the complaint: "All that leaves me around 1 GB for my photos after I install all the essential (social, chats, maps, taxi, banks etc) apps."

I won't lie, those 275 megabytes of LinkedIn raise questions for me too. But I remember how in 2010 Habr [reported](https://habr.com/ru/post/109616/) (in Russian) that Alfa-Bank, a Russian bank, had released a mobile app. It weighed 30 megabytes, a size that wouldn't raise any questions at all today. But back then, the comments said:

![](../images/software2020/04.jpg)

Do you know why? Back then, a Russian user might be carrying, for example, an [HTC Hero](https://en.wikipedia.org/wiki/HTC_Hero). Let's look at its specs: "storage — 512 MB, 165 for applications". 165 megabytes in total for all installed apps! Under those conditions you constantly had to choose which ones were more important and which you could live without. And to install a 30-megabyte one, you'd have to remove several others at once. It was painful.

And if we could go back to 2010, walk up to the people feeling that pain and tell them the 2018 line "that leaves me around 1 GB for my photos", I think they'd beat us up. Those words would sound not like a complaint but like mockery and bragging.

And even since 2018, when that complaint appeared, things have improved: today the budget Xiaomi Mi A3 comes with 64 gigabytes in its base version, so after installing apps there will clearly be far more than one gigabyte left.

Yes, apps have grown severalfold over 10 years. But storage over the same period has grown HUNDREDS of times. So life has become dozens of times better.

And do you even remember what it was like to use a smartphone in 2010, and how many different "everything is slow" pains there were?

- Little RAM meant apps constantly had to be launched "from scratch" instead of instantly switching to one already running.
- And underpowered processors launched them from scratch very slowly.
- I don't even want to remember the speed of mobile internet.
- Transferring photos to a computer and backing up your phone had to be done over a cable, and in the days of USB 2.0 that was agonizingly slow.

Using a smartphone looked like constant waiting: whatever you wanted to do involved periods of "standing there, staring at the screen". If you were out and needed a map, you stood still and first waited for the app to deign to launch, then waited for the map in it to deign to load. And on top of that you paid noticeably for the data it used.

Compared to all that, we now live in paradise, yet we complain actively. It looks like "first world problems", something like "I want to read Twitter lying down, holding my phone above my face, but then I might accidentally drop it on myself". Well, my sympathies, but saying "everything has gotten worse" in that situation seems disrespectful to both the past and the present.

> Overall conclusion: loud claims that "everything used to work faster and better" turn out to be obviously untrue. It seems that their authors' memory nostalgically serves up only the pleasant parts of the past and suppresses the unpleasant ones. A great deal was much slower and worse.

---

## Not understanding the "internals"

There's another typical situation. People say "software is ever more bloated and sluggish, even though almost nothing changes for the better for the user", and yet they aren't quite aware of what's actually going on in there.

A small illustrative example. In 2018 there was a [much-discussed piece](https://tonsky.me/blog/disenchantment/) by Nikita Prokopov about "software disenchantment", and among other things it said: "Google Play Services, which I do not use (I don't buy books, music or videos there)—300 MB that just sit there and which I'm unable to delete."

Reading that, you want to fill up with righteous anger, yes. But there's a catch: Google Play Services actually has nothing to do with "buying books". It includes many different APIs, and, as Wikipedia [puts it](https://en.wikipedia.org/wiki/Google_Play_Services), "All major Android services are controlled by Google Play Services". So, in all likelihood, Nikita uses this software actively without knowing it: Google just gave it a confusing name.

My goal here isn't to criticize a specific post but to show a general approach: we often declare "apps have bloated/slowed down for no good reason" without fully understanding the reasons. Something was added to an app, its developers have detailed information about what exactly and why, and we don't, yet for some reason we consider ourselves more competent on the matter than they are.

And there's a lot inside that isn't obvious from outside. Take text editors, for example: people have been making them since time immemorial on the weakest hardware, everything about them has long been clear, and there's nothing there to lag, "what could be simpler". So from the outside it looks like this: if something doesn't respond instantly, it's clumsy developers who have forgotten what humanity already knew how to do. But if you dig into the topic (we once published a [Habr post](https://habr.com/ru/company/jugru/blog/424763/) about it, in Russian), you suddenly discover lots of non-obvious nuances, and the words "what could be simpler" stop sounding convincing.

Or here's another one. News about mobile operating systems often gets this reaction: "They haven't done anything useful in the last eight years or so. Every year they roll out a new version with great fanfare, it's bigger than the previous one, but the only difference I see is new emoji. I couldn't care less about those emoji, give me back the old version, it was better."

![](../images/software2020/05.png)

Listen, every IT person seems to know from experience: you can spend a huge amount of effort on a well-justified backend refactoring and the user won't even notice, or you can change a couple of icons in the interface in half an hour and heated discussions will break out among users. So we know that only some changes are visible "from the outside", and often not the most important ones. Why, then, don't we realize that if the only thing we ourselves notice in a new OS version is the emoji, that says more about us than about the OS?

Take, for example, Project Treble in Android 8.0. Android famously has a big problem: while iPhones easily update to new OS versions, Android phones usually stay forever on the preinstalled version, because their manufacturers don't want to bother. So Google undertook a massive rework of the whole architecture to make manufacturers' lives easier and encourage updates. And although Treble didn't solve the problem completely, the statistics show a noticeable improvement. So Google put a lot of work into fighting a long-standing problem (refactoring a colossus like that is no walk in the park), and managed to partially improve the situation. I think that's exactly what a company should do: deal with long-standing problems. They did the right thing.

Now tell me: unless you're a mobile developer, have you even heard of it? When you first picked up a phone with Android 8.0+, did it affect your opinion of the new version at all? Hardly, because in the first months of using a phone it doesn't show for the user at all. You can only notice it later, when a new version of Android comes out. And only if your phone's manufacturer turns out to be among those Treble prompted to update their devices. And even then the user may not realize that Google deserves credit for the update, and keep saying "they haven't done anything useful in eight years".

And this situation is typical: the "underwater part of the iceberg" is generally large. When Android introduced Adaptive Battery ("smart" detection of which apps may drain the battery in the background), did you measure whether your phone's power consumption changed? When Google Play Protect looks after your security in the background, do you remember that it didn't used to exist? When support for the AV1 video codec was added, did you consider that this codec very likely represents the future and such support is useful? Or do you just pick up your phone, and the emoji catch your eye while AV1 support doesn't?

After this post came out, a great [thread](https://threadreaderapp.com/thread/1242983413642076160.html?refreshed=yes) (in Russian) appeared from [lany](https://habr.com/ru/users/lany/) about how software bloats largely because of handling rare situations. And here's what follows: for the 1% of cases where these situations arise, everything has become much better, but the 99% of people who never run into these rare situations can't properly appreciate the changes.

> This is needed extremely rarely. But it's already hundreds of kilobytes compressed (the clock now depends on an unzipping algorithm) and megabytes uncompressed. Of course, all of this has to be updated regularly. An update mechanism appears in the clock. Next up, leap seconds.
>
> — Tagir Valeev (@tagir_valeev) [March 26, 2020](https://twitter.com/tagir_valeev/status/1242987538597412866) (translated from Russian)

It follows that when we lump together all "bloated and sluggish apps" and complain about them, in many cases there were objective reasons. Somewhere, people during working hours carefully weighed all the pros and cons, discussed them with each other, and concluded that "the pros outweigh the cons". And then we come along, with no idea what was on the scales, with no intention of spending time on careful study, see only the changed size, and confidently conclude that "everything has gone downhill".

> Overall conclusion: some of the claims about "pointlessly bloated software" come from misunderstanding. And making such claims without carefully researching the reasons isn't the smartest strategy.

---

## Attention to performance

Claims about "software gone bad" sound as if developers used to economize on computing power, and now they all couldn't care less about optimization. As in: all that matters is that it works, and if the hardware requirements turn out high, Moore's law will sort it out somehow. If the code runs slowly, eats memory like there's no tomorrow and takes up a lot of space, that'll do; nobody's going to worry about it and improve anything.

Listen, that's simply not true. As a single example: Facebook Messenger was recently [rewritten](https://techcrunch.com/2020/02/28/messenger-removes-discover), and reportedly its performance doubled and its size shrank fourfold. And regarding the 275 megabytes of the LinkedIn app mentioned above: I just checked and saw "195.4 MB" in the App Store, so it seems they've shrunk it by almost a third too. So both companies clearly thought about resource consumption and devoted a lot of effort to reducing it, effort that could have gone into "cranking out features".

And since my job is connected with developer conferences and I cross paths with many developers (from different stacks, too), I see which topics concern them. What they listen to talks about, what they discuss and write posts about.

And performance is definitely one of those topics. From talk titles like «[Optimizing iOS app launch time](https://www.youtube.com/watch?v=REaGfwq3Q5Y)» (in Russian) you can see that developers are willing to spend 60 minutes listening about milliseconds.

People talk about performance everywhere, whether in the JavaScript world («[JavaScript performance through a spyglass](https://www.youtube.com/watch?v=HPFARivHJRY)») or in mobile development («[How to fit a million stars into an iPhone](https://habr.com/ru/company/jugru/blog/427845/)»), both in Russian. But the backend talks about it most. I think that's because users buy their smartphones themselves, whereas on the backend the company pays for the computing power, so there's a strong financial motivation to optimize.

I recently ran a simple experiment: I opened the program of our Java conference [JPoint](https://jpoint.ru/?utm_source=habr&utm_medium=493178) and looked at how many talk descriptions mention something about performance. Later, because of the coronavirus, we moved the conference to June, so the program may change, but the results are telling anyway. Here they are:

- "This talk will be about tuning Producer performance"
- "We'll look at methods for optimizing file I/O"
- "Maybe for one of your modules you want more performance than you'll ever be able to squeeze out of Java?"
- "What safepoint-related optimizations does the HotSpot JVM make? What should developers keep in mind to avoid unwanted pauses?"
- "Project Valhalla, inline types and everything around them, from the programming model to performance"
- "Optimize query performance, throughput and memory consumption"
- "The talk is a detailed breakdown of how writing to the Apache Cassandra database works from a performance point of view"

Listen, if I'd run this experiment as a drinking game, I'd have been drunk by the end of it. It's plain to see: Java developers care about making their code not just work, but work fast.

What's more, they often care about it too much! I've heard more than once from people who work closely on performance that it's easy to overdo it here. For example, for the sake of a negligible performance gain, people use dirty hacks that end up creating more problems than they solve. Well, that was covered in Aleksey Shipilёv's excellent keynote at JPoint 2017, which we [transcribed](https://habr.com/ru/company/jugru/blog/338732/) for Habr (in Russian).

![](../images/software2020/06.png)

> To sum up: while the internet laments that "developers have gotten lazy and stopped thinking about slowness altogether", in reality many developers think about it *more than they need to*.

---

## Meaningfulness and expediency

And now, I think, the most important point.

Yes, over time apps have come to require more resources, sometimes by orders of magnitude. Yes, projects started pulling in much more, even things that aren't really needed, instead of spending time isolating the "strictly necessary". That's true.

But I believe that bigger apps don't make today's developers incompetent fools. Quite the opposite:

**Developers would be fools if apps had NOT grown.**

Imagine a world where hardware developed over recent decades just as it did in ours, but the approach to software development didn't change. Programs there still fit on a floppy disk, even though nobody uses floppy disks anymore. In the name of performance, more or less everything is written in C. All developers constantly go down as close to the hardware as possible and know every spot where a couple of bytes can be saved. And although Retina screens arrived, nobody made app icons more detailed, so they wouldn't get heavier. In short, a festival of optimization and careful use of resources. Everything that people now mourn as "lost craftsmanship".

Do you know what impression this picture makes on me? A large family was forced to live in one small room, so they learned to place things with millimeter precision and mastered the secret art of making five-tier bunk beds. Then they moved into a spacious apartment with many rooms, but out of habit occupied only one room there and left all the others empty. People are still living on top of each other.

Question: doesn't this seem like madness to you? If it became possible to give everyone plenty of space, why save it? Who benefits from the ancient art of five-tier beds if there's still nowhere to invite a guest? Isn't it time to master the new art of choosing a king-size bed?

It's the same in software. If, in an era when even budget smartphones have 64 gigabytes, we worry that "the Kotlin runtime will increase our app by a megabyte", then we'll turn into that family. Relax: space exists so that something can be in it. If it goes to waste, that doesn't make anyone better off. If there's now plenty of space and something calls for a grand piano, then go ahead and put it in without worrying about square centimeters.

Slack is that grand piano. Okay, it eats a lot of memory, but have you heard non-IT people complain about it the way they once complained about Photoshop? My impression is that ordinary users already have enough space for this "piano" not to stop them "walking across the room". Yes, you could replace it with an upright and save space. But if you live in a palace, and the palace keeps getting bigger over the years, why?

I think it's mostly IT people who worry about Slack, because they need RAM for other heavy tasks. But IT people are a separate story: to extend the apartment metaphor, they're people who have turned their apartment into a workshop. Well, yes, give them any palace and every room will be taken up by something very important. Then the piano can get in the way: you could put a lathe there instead. But most people in the world live differently: they don't need lathes at home, and for their way of life there are already enough resources.

In that situation, feverishly avoiding everything that takes up memory once there's plenty of it is like those mobile task managers where users kill running apps to "free up RAM". The makers of mobile platforms have said many times: "Stop, you madmen. The system will kill apps itself if memory runs short; why kill them before that? What's the point of buying a smartphone with lots of RAM and then keeping it empty and not using what you paid for?"

![Looks optimized. Would you like to live here?](../images/software2020/07.jpg)
*Looks optimized. Would you like to live here?*

And I'm also reminded of the story of the "Y2K bug". One of the IT people from the mid-20th century recalled in old age: "We were among those who created it. Back then we saved every byte. And when we came up with the idea that a year could be stored as two digits instead of four, we felt very clever. We saved two bytes in lots of places! And only toward the end of the century did the consequences become clear."

Yes, at the time, writing the year as two digits must have looked like a sensible decision. And it embodies everything that advocates of the "careful" approach champion. Here, care for resources truly reached its limit.

But then, many years later, other people had to spend a lot of resources dealing with the consequences of that decision and preventing problems.

And now that the two saved bytes won't help anyone and the negative consequences are known, it would be very strange to store the year that way.

So: much of what we're tempted today to praise as "sensible saving of resources" will in the future look like the same kind of "penny-pinching" that cost more resources than it saved. For example, because a developer's time is also an extremely valuable resource, and it often isn't included in the calculation. If you went all-in on data alignment, and your app became a little smaller and faster, but you spent a week on it that could have gone into a useful feature, did you make things better or worse for the user?

> Yes, it's very tempting to feel "I'm smart and thrifty, I know how to save resources where others squander them". It's a pleasant feeling.
>
> And pleasant feelings matter. If a developer is sick of a project, that's no good: it will hit their motivation and make things worse for everyone.
>
> But you have to be able to tell where something is useful for everyone (directly making users happier) and where it's the pleasant feeling of scratching your own ego. And not pass one off as the other.

---

## A conciliatory conclusion

I anticipate objections in the comments: "but task X really does run slower for me than 13 years ago, give me back my 2007".

Don't get me wrong: I'm not trying to say such tasks don't exist. [They do](https://danluu.com/input-lag/). And excessive use of dependencies exists too. And bloatware exists. When I hear that Photoshop has video editing, I get the same "WHY" feeling as you do. When I read that creating any app with create-react-app immediately means 4,304 directories with 28,678 files in them, I too wonder whether we've taken a wrong turn somewhere. There are many real problems worth talking about.

My only objection is that around these problems, some kind of radical sect arises, believing in an imminent end of the world caused by software bloat. This sect rewrites history ("everything used to work faster!"), misunderstands what's happening ("why has Windows grown so much over the years, nothing much has changed in it"), says undeserved things about developers ("they don't want to optimize anything") and goes to the extreme of "let's save every byte, even when it makes things worse for users". Let's not do that.

My objections to the radical position, of course, also came out somewhat radical (just in the opposite direction). They can be nitpicked too, and they can be called a sect too. But the goal of this post isn't for every word of mine to be taken as the ultimate truth. Its goal is this: for people to get drawn into sects a little less.

> The main conclusion is boring and banal, but no less true for it: it all depends on the specific situation. Optimizations are neither absolute evil nor absolute good. They can help and harm at the same time. There are situations where optimizations are clearly worth it, and situations where they clearly aren't. And there are in-between situations where different people will judge "worth it or not" differently, none of them will be more right, and that's fine.
>
> And if anyone, including me, tells you otherwise, they're a cultist: send them packing.
