"""Generate narration audio for Biology Level 3 site using ElevenLabs TTS."""

from elevenlabs import ElevenLabs
import os
import time

API_KEY = "28c9a007ab7691a53034447c954a6a68e59d887445cb5dfe02c0dcc92198edbc"
VOICE_ID = "tghQO4ccpTi1eriPYDPW"  # Eliot (professional)
MODEL_ID = "eleven_multilingual_v2"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "public", "audio")

# --- Narration scripts: natural spoken versions, paraphrased for voice ---

NARRATIONS = {
    # ── Week 3: How to Watch Videos ──────────────────────────────────────
    "how_to_watch": """
How to watch videos to actually learn.

OK, here's the thing. Just pressing play and letting a video run in the background? That's basically doing nothing. Research shows that students who passively watch videos barely learn more than students who never watched at all. So if you're going to spend the time watching, you might as well get something out of it. Here's how.

First — before you even press play — read the description underneath the video and ask yourself what you already know about the topic. This is called the pre-question effect. Having a question in your head before you watch primes your brain to notice the answers. It's like giving your brain a shopping list before you walk into the supermarket.

Second — while you're watching — pause every couple of minutes. Try to predict what's coming next. After a key point, look away from the screen and say the idea back to yourself in your own words. If you can't explain it, rewind and watch that bit again. This is retrieval practice — the act of pulling information out of your memory is actually what makes it stick, not just putting it in.

Third — and this is a big one — draw things. Don't just write notes in sentences. Sketch a diagram. Draw a woodlouse in a choice chamber. Draw arrows showing how taxis movement differs from kinesis. This is called dual coding — when you combine words and pictures, you create two separate memory traces in your brain, which makes the information much easier to recall later. A quick rough diagram is worth more than three paragraphs of neat writing.

Fourth — playback speed. Research shows that watching at one-and-a-half-times speed is fine for comprehension. Your brain can keep up. But two-times speed significantly hurts retention when you're learning new material. So first time through, stick to normal speed or one-and-a-half-times. Rewatching for revision? One-and-a-half-times is totally fine.

Fifth — the moment the video ends, close your laptop, flip your phone over, and write down everything you can remember. This is called a brain dump, and it's one of the most powerful study techniques there is. Don't worry about getting everything perfect. The effort of trying to recall is exactly what builds the memory. Then check what you missed, and focus on those gaps next time.

And finally — don't binge. Watching all twelve videos in one sitting might feel productive, but it doesn't produce lasting memory. The spacing effect tells us that spreading your watching across multiple days, even just two or three videos per session, leads to dramatically better retention. A little bit of forgetting between sessions is actually a good thing — it makes the next review harder, and that effort is what makes it stick.

So the bottom line is this. Watching a video is not studying. Watching a video while pausing, predicting, sketching, and testing yourself — that is studying. The students who do best aren't the ones who watch the most videos. They're the ones who think the hardest while watching.
""",

    # ── Week 4: Why We Write Answers ─────────────────────────────────────
    "week4_why_writing": """
Why are we doing this? Good question. There are two reasons I want you to write your answers here rather than just scribbling them in a notebook.

First, it gives you a record of your own thinking. Once you download the PDF, or copy your answers into OneNote, you've got a snapshot of how you explained these concepts today. Come back to it in a few weeks and you'll be able to see how much clearer your writing has become. That's genuinely useful revision.

Second, writing well matters in Biology. The external exams reward clear, precise explanations. I'll be reading through your submissions in Teams Assignments so I can give you feedback on how to tighten up your answers — not just the science, but how you communicate it. The earlier we start practising that, the better you'll be by the time exams come around.

So: answer the questions, download the PDF, and upload it to the Teams Assignment. If you'd also like a copy in your OneNote, use the Copy All Answers button and paste it straight in.
""",

    # ── Week 6: Physiological Triggers of Migration ───────────────────────

    # 1. Lesson 1 intro — the big picture
    "week6_lesson1_intro": """
OK, so this is the lesson where we get into the really cool biology behind migration. Up until now you've learned what migration is and why it evolved. Now we're asking a different question: how does a bird actually know when it's time to go?

And here's the key thing. It's not because it gets cold. That's the number one mistake students make in the exam. Think about it — if birds waited until it got cold, a warm autumn would completely throw them off. They'd leave too late, miss the good weather for travelling, and die.

Instead, birds use day length — photoperiod. Day length changes on exactly the same schedule every single year. It's like a clock that never drifts. So evolution has wired birds to respond to day length as their primary trigger.

But it gets better. They also have an internal biological clock — a circannual rhythm — that runs on roughly a yearly cycle. The day length signal keeps that internal clock calibrated. And when the clock says it's time, it kicks off a whole cascade of hormonal changes that physically rebuild the bird's body for migration. We're talking fat storage, muscle growth, organ shrinkage — the bird literally becomes a different animal.

By the end of this lesson, you'll understand that entire cascade from light hitting the eye through to the moment the bird takes off. That's what we're building toward.
""",

    # 2. Photoperiod — why it matters
    "week6_photoperiod": """
Let me unpack this photoperiod idea because it's central to everything in this lesson.

Imagine you need to set an alarm that goes off at the same time every year. You could use temperature, but temperature is unreliable — some years it's warm in May, some years it's freezing. You could use food availability, but that fluctuates too. The one thing that is absolutely, mathematically identical on the same date every year is day length. June the twenty-first always has the same number of daylight hours, whether it's a warm year or a cold one.

So that's what birds have evolved to use. When days reach a specific length — what we call the critical photoperiod — it's like flipping a switch. The bird's brain detects the day length, the pineal gland changes how much melatonin it produces, and that melatonin signal tells the hypothalamus what season it is. The hypothalamus then fires up the whole hormonal programme.

Now, there's a beautiful detail here for your exam answers. Each species — and even each population within a species — has its own critical photoperiod. A kuaka population in one area might have a slightly different trigger point from a population further north, because the "right" departure date depends on local conditions. That critical photoperiod is genetically determined. So when the exam asks why photoperiod is the primary trigger, you say: it's predictable, it's consistent between years, and it can be precisely calibrated to local conditions through natural selection. That's an Excellence-level answer.
""",

    # 3. Tsoogunruhe and the internal clock
    "week6_zugunruhe": """
Tsoogunruhe. Great word, terrible to spell. It's German for "migration restlessness" and it's one of the most fascinating things in animal behaviour.

Here's the experiment that proved it. In 1967, a researcher called Stephen Emlen put migratory birds into funnel-shaped cages lined with ink-sensitive paper. The bird stands at the bottom, hops and flutters, and its inky footprints record which direction it's trying to go.

During migration season, the footprints cluster in the direction of the bird's normal migration route. Outside migration season, the footprints are random — the bird isn't trying to go anywhere in particular. And crucially, the duration of this restless behaviour matches how long the bird's migration normally takes. It's as if the bird has an internal programme that says "fly south for three weeks."

Now here's where it gets really compelling. Eberhard Gwinner took garden warblers, raised them from eggs in completely constant conditions — same light, same temperature, same food, no seasonal cues whatsoever — and the birds still showed annual cycles of fat storage and Tsoogunruhe at roughly the right time of year. The cycle wasn't quite twelve months though — it drifted to about ten or eleven months. So the internal clock exists, but it needs day length as a time-giver — a Zite-gaber — to stay synchronised with the real calendar.

For your exam, the distinction between the endogenous clock and the Zite-gaber is what gets you into Excellence territory. The clock generates the timing. Photoperiod makes it precise.
""",

    # 4. NZ Case Studies
    "week6_nz_cases": """
Let me bring these three New Zealand species to life for you, because each one illustrates something different about how migration physiology works.

First, kuaka — the bar-tailed godwit. This is the bird that makes the most extreme body transformation of any migrant. In just a few weeks, it nearly doubles its weight, packs on so much fat that more than half its body mass is fuel, grows its flight muscles by thirty percent, and — here's the wild part — deliberately shrinks its own stomach and intestines. Why? Because it won't eat for nine days straight, so carrying a full digestive system is dead weight. It's like stripping everything unnecessary out of a race car.

Second, tuna — the longfin eel. This one's arguably even more dramatic. After living quietly in a New Zealand river for twenty, fifty, sometimes over a hundred years, the eel undergoes a complete metamorphosis. Its eyes double or triple in size and shift to deep-sea visual pigments. Its skin turns silver for ocean camouflage. Its gut completely degenerates — it will never eat again. And its gonads swell to fill most of its body cavity. All of this is triggered by a surge of gonadotropins from the pituitary. And remember from Week 3 — the glass eel swam upstream using positive rheotaxis. The silver eel reverses that completely, heading downstream. Same stimulus, opposite response, switched by hormones.

Third, tītī — the sooty shearwater. What's remarkable here is the precision. These birds fly a sixty-five thousand kilometre figure-eight around the Pacific, and most of them depart their breeding colonies within a two-week window each year. That precision comes from a strong circannual clock tuned by photoperiod. And here's a lovely connection — Ngāi Tahu muttonbirders have been recording tītī departure and arrival times for centuries, and their observations match modern satellite data almost exactly.
""",

    # 5. Hyperphagia and fat as fuel
    "week6_hyperphagia_fuel": """
Right, let's talk about eating. Hyperphagia literally means excessive eating, and it's the first visible sign that a bird is getting ready to migrate.

The trigger is corticosterone — the bird's stress hormone. As day length changes and the hormonal cascade kicks in, corticosterone rises and does three things: it cranks up appetite by acting on the hypothalamus, it tells the liver to switch into fat-production mode, and it extends the hours the bird spends foraging. Some hyperphagic birds feed almost continuously during daylight.

The result is spectacular. A kuaka that normally weighs two hundred and fifty grams will hit four hundred and fifty or even five hundred grams at departure. That's like you going from seventy kilos to a hundred and forty in a month.

Now, why is all that fuel stored as fat and not as carbohydrate? Three reasons, and knowing all three is what gets you to Excellence.

One — energy density. Fat gives you thirty-nine kilojoules per gram. Carbohydrate gives you seventeen. So gram for gram, fat delivers more than double the energy. When you're carrying all your fuel while flying, that's enormous.

Two — water. Glycogen, the stored form of carbohydrate, needs three to four grams of water for every gram stored. Fat stores dry — almost no water needed. If a kuaka tried to carry its fuel as glycogen, it would need to be five to eight times heavier. It couldn't get off the ground.

Three — and this is the one most students miss — when fat is burned, it actually produces water. About one gram of water for every gram of fat oxidised. For a bird flying non-stop over the Pacific Ocean for nine days with no access to fresh water, that metabolic water is literally what keeps it alive.

So fat isn't just efficient fuel. It's also a water source. That third point is your Excellence separator.
""",

    # 6. Body remodel — the radical trade-off
    "week6_body_remodel": """
This is where migration biology gets genuinely astonishing. It's not just about eating more and storing fat. Migratory birds physically rebuild their bodies before departure.

Think about a car analogy. If you were preparing a car for a race across a continent, you'd want a bigger, more powerful engine, a more efficient fuel system, and you'd strip out everything you don't need — back seats, spare tyre, stereo. That's exactly what migratory birds do, but with their own organs.

The flight muscles — the pectorals — grow by fifteen to forty percent. But it's not just getting bigger. The number of mitochondria inside each muscle fibre increases, so there's more capacity for aerobic respiration. Myoglobin — the oxygen-carrying protein in muscle — goes up, so more oxygen reaches those mitochondria. And the enzymes for burning fat are upregulated, turning the muscle into a specialised fat-burning machine. It's a complete engine overhaul.

Meanwhile, the organs the bird won't need during flight are shrinking. Stomach and intestines lose forty to fifty percent of their mass. The liver shrinks by a quarter. Kidneys shrink by twenty percent. But the heart grows by twenty to thirty percent, because it needs to pump more blood to those bigger muscles.

At departure, a kuaka is roughly fifty-five percent fat, thirty percent muscle and skeleton, eight percent heart, lungs and blood, and only about seven percent everything else. It's basically been redesigned as a flying fuel tank.

The exam loves this topic. But don't just describe the changes — explain them as trade-offs. Gut shrinkage isn't a defect; it's adaptive. The bird trades digestive capacity, which it won't need, for reduced mass, which directly increases its flight range. That trade-off framing is what examiners are looking for at Merit and Excellence.
""",

    # 7. Kuaka — the incredible flight
    "week6_kuaka_flight": """
Let me put everything together with the kuaka's actual flight, because this is where all the physiology we've covered comes to life.

In 2007, a female kuaka called E7 was tracked by satellite as she flew eleven thousand six hundred and ninety kilometres from Alaska to the Miranda coast near Thames, New Zealand. She did it in eight point one days. Non-stop. No food, no water, no rest. Since then, even longer flights have been recorded — over twelve thousand kilometres.

Think about what that requires. Continuous flapping at about fifty-six kilometres per hour. Burning fat at nearly one percent of body mass every hour. Producing water from that fat to stay hydrated. Possibly sleeping with one half of the brain at a time while the other half keeps flying — though we're still researching that.

And when she arrives, she's lost about half her departure weight. Virtually zero fat remaining. She's used everything.

Here's what I want you to take away for the exam. The kuaka's flight isn't just impressive as a number — it's the endpoint of every single physiological process we've studied this week. Photoperiod triggered the hormonal cascade. Corticosterone drove hyperphagia and fat storage. The body remodelled — muscles grew, guts shrank, the heart enlarged. Fat was chosen as fuel because of its energy density, dry storage, and water production. And an endogenous clock, calibrated by photoperiod, determined the precise departure window.

If you can tell that story — from light hitting the eye all the way through to the bird arriving in New Zealand — and explain the biological significance at each step, you're writing an Excellence answer. That's the narrative arc the examiners are looking for.
""",

    # ── Week 3: Simple Animal Responses ───────────────────────────────────

    # 1. Taxis vs Kinesis — the core concept
    "week3_taxis_kinesis": """
Right, taxis and kinesis. These are the two types of simple innate response, and the distinction between them is one of the most common exam questions you'll face. So let's get it absolutely clear.

Both taxis and kinesis are about an animal moving in response to a stimulus. The crucial difference is whether the animal knows which direction the stimulus is coming from.

Taxis is directional. The animal detects where the stimulus is and moves towards it or away from it. A moth flying towards a light — that's positive phototaxis. The moth knows where the light is and heads straight for it. There are two ways animals do this. Klinotaxis is where the animal has one receptor and swings its body side to side to compare — like a maggot waving its head left and right to figure out which side is brighter. Tropotaxis is where the animal has paired receptors, one on each side, and compares both sides simultaneously — like a barnacle larva detecting chemical concentration on its left and right at the same time.

Kinesis is non-directional. The animal can't tell where the stimulus is coming from. Instead, it changes how it moves. There are two types. Orthokinesis is a change in speed — woodlice move faster in dry conditions and slow down in humid ones. They don't know which way the moisture is, they just keep moving until they stumble into somewhere damp and then stop. Klinokinesis is a change in turning rate — a flatworm turns more often in bright light and moves in straighter lines in the dark. The result is the same — it ends up in a dark area — but not because it aimed there.

Here's the exam key. Both taxis and kinesis get the animal to a better place. But they do it through completely different mechanisms. Always explain the mechanism, not just the outcome.
""",

    # 2. The Eight Stimuli — vocabulary
    "week3_stimuli": """
OK, quick vocabulary lesson. There are eight stimulus types you need to know, and each one has a prefix. You combine the prefix with "taxis" or "kinesis" to name the response.

Photo means light. Thermo means temperature. Gravi or geo means gravity. Chemo means chemicals. Thigmo means touch. Hydro means water or moisture. Rheo means water current. And tropho means food or nutrients.

So if you see a moth flying towards a light, that's positive phototaxis — photo for light, taxis because it's directional, positive because it's moving towards. If a woodlouse speeds up in dry air, that's hydrokinesis — hydro for moisture, kinesis because it's non-directional.

The trick for the exam is to always use the correct terminology. Don't just say "the eel swims against the current." Say "the eel exhibits positive rheotaxis" — rheo for current, taxis because it's directional, positive because it moves into the current. That precise language is what gets you marks.
""",

    # 3. NZ Examples — bringing species to life
    "week3_nz_examples": """
Let me walk you through the New Zealand examples because these are the ones that could appear in your exam.

First, the glow-worm — Arachnocampa luminosa. This is a brilliant example of how one organism exploits another's innate response. The glow-worm larva produces light in caves, and its prey — midges and moths — exhibit positive phototaxis. They fly straight towards the glow and get trapped in sticky silk threads. The glow-worm is essentially hacking its prey's hardwired behaviour.

Second, tree weta. These are nocturnal and show strong negative phototaxis — they actively avoid light. Research at Maungatautari found an eighty-seven point five percent reduction in weta activity in areas with artificial lighting. Males were particularly affected. This has real conservation implications for light pollution near native bush.

Third, paua larvae. These tiny larvae swim towards chemicals released by coralline algae on rocks — positive chemotaxis. More than eighty-eight percent of larvae settled within one day when exposed to the right algal chemicals. This ensures they land on suitable habitat near adult feeding grounds. It's a critical step in paua population sustainability.

And fourth, the longfin eel — tuna. As glass eels returning from the ocean, they swim against the river current — positive rheotaxis. But later in life, the adults reverse this completely and head downstream to the sea. Same stimulus, opposite response — and that switch is driven by hormones, which you'll learn about in later weeks.
""",

    # ── Week 4: Pheromones & Navigation ───────────────────────────────────

    # 4. Pheromones — what they are
    "week4_pheromones": """
Pheromones. In Week 3 you learned about chemotaxis — movement towards or away from chemicals. Pheromones are one of the most important chemical signals in nature, and they take that concept to a whole new level.

A pheromone is a chemical secreted by one animal that triggers a specific response in another member of the same species. That's the key distinction from hormones — hormones work inside the body, pheromones work between individuals, through the external environment.

Now here's the exam-critical distinction. There are two types of pheromone, and they work in completely different ways.

Releaser pheromones trigger an immediate behavioural response. They act on the nervous system — fast and stereotypic. An ant releases an alarm pheromone and other ants scatter instantly. A female moth releases a sex pheromone and males fly towards her within seconds. These are rapid, short-term behavioural changes.

Primer pheromones trigger a slow physiological change over days or weeks. They act on the endocrine system, altering hormone levels. The classic example is honeybee queen substance. The queen produces a pheromone that suppresses ovary development in all the worker bees. It doesn't make them do anything immediately — it gradually changes their physiology.

And here's the exam favourite: honeybee queen mandibular pheromone is both. It immediately attracts workers to groom the queen — that's a releaser effect. And it suppresses their ovary development over weeks — that's a primer effect. Same chemical, two different mechanisms. If you can explain that in an exam, you're showing real understanding.
""",

    # 5. Sun Compass — the elegant mechanism
    "week4_sun_compass": """
Sun compass navigation. This is one of those topics where the biology is genuinely elegant.

Many animals use the sun's position to navigate. But here's the problem — the sun moves across the sky. It's in the east in the morning, overhead at midday, in the west in the evening. So if you're using the sun as a compass, it's only useful if you also know what time it is. Otherwise a bee trained to find food to the east in the morning would search to the south at midday.

The solution is a time-compensated sun compass. The animal has an internal circadian clock that tracks the time of day, and it uses that clock to adjust for the sun's apparent movement. The sun is here at nine AM, there at noon, over there at three PM — and the animal's clock compensates automatically.

The proof comes from a beautiful experiment. Scientists kept homing pigeons in artificial light cycles shifted by six hours. When released, the clock-shifted pigeons flew ninety degrees off course — exactly the error you'd predict if their internal clock was six hours wrong. The sun was in one place, but the pigeons' clocks said it should be somewhere else, so they miscalculated the direction.

That experiment is exam gold. It proves two things at once: that the animals are using the sun for direction, and that they're using an internal clock to compensate for the sun's movement. If either piece is missing — no sun or no clock — the navigation breaks.
""",

    # 6. Magnetic Navigation — cutting-edge science
    "week4_magnetic_nav": """
Magnetic navigation is probably the most mind-blowing topic in this whole course. Animals can detect Earth's magnetic field — and they use it for both compass direction and position.

Let me explain what information the magnetic field actually provides. Earth's field lines emerge vertically at the poles and run horizontally at the equator. The angle of these field lines — called the inclination or dip angle — tells an animal whether it's heading poleward or equatorward. That's a magnetic compass.

But it gets better. Both the total field strength and the inclination angle vary in predictable patterns across the globe. If an animal can detect both, it can estimate its latitude and longitude — a magnetic map. Sea turtles have been shown to do exactly this.

Now, how do they detect it? There are two proposed mechanisms, and knowing both is important for Excellence answers.

First, magnetite crystals. Tiny crystals of naturally magnetic iron oxide have been found in the beaks and nasal tissues of birds. These crystals physically rotate in response to the magnetic field and stimulate nearby nerve cells.

Second, cryptochrome proteins. These are molecules in the retina of birds that are activated by blue light and form what are called radical pairs. The chemistry of these radical pairs is influenced by the magnetic field. This might mean birds can literally see the magnetic field — as a visual pattern overlaid on their normal vision.

For the exam, don't just say animals sense the magnetic field. Explain what information it provides — inclination for direction, intensity plus inclination for position — and how it's detected. That level of mechanism is what separates Excellence from Merit.
""",

    # ── Week 5: Waggle Dance, Homing & Migration ─────────────────────────

    # 7. Waggle Dance — how it works
    "week5_waggle_dance": """
The waggle dance. This is genuinely one of the most remarkable behaviours in the animal kingdom — a tiny insect communicating the location of food using a symbolic language.

When a forager bee finds a good food source, she returns to the hive and dances on the vertical surface of the honeycomb. The dance encodes three pieces of information: direction, distance, and quality.

Here's how direction works — and this is the clever bit. The bee can't point and say "that way." She's dancing on a vertical comb inside a dark hive. So she uses gravity as a stand-in for the sun. If she runs straight up the comb during the waggle phase, that means the food is in the direction of the sun. Straight down means directly away from the sun. Sixty degrees to the right of vertical means sixty degrees to the right of the sun's direction from the hive.

She's transposing a horizontal outdoor map onto a vertical surface using gravity. That's extraordinary for a brain the size of a pinhead.

Distance is simpler. The longer the waggle run lasts, the further away the food is. About one second of waggling equals roughly one kilometre. And quality? The more vigorously she dances and the more circuits she does, the richer the food source.

The other bees can't see the dance — it's dark in the hive. They follow the dancer with their antennae, feeling the movements, and they pick up the scent of the flowers from the dancer's body.

Karl von Frisch decoded all of this using glass-walled observation hives and numbered bees. He won the Nobel Prize for it in 1973 — the first and only Nobel awarded for animal behaviour research.
""",

    # 8. Homing — the four navigation systems
    "week5_homing": """
Homing. This is different from the simple orientation behaviours you learned in Week 3. Taxis gets a woodlouse to a damp area. Homing gets a seabird back to its specific nest on a specific island after months at sea and thousands of kilometres of ocean. It requires navigating to a remembered goal, often across unfamiliar terrain.

Animals use four main types of navigation cue, and most long-distance navigators use several of them together.

First, topographical cues — visual landmarks like mountains, coastlines, rivers. These are most useful close to home. A pigeon recognises the landscape near its loft.

Second, celestial cues — the sun compass you learned about in Week 4, and the star compass for night navigation. Both need clear skies.

Third, magnetic cues — Earth's magnetic field. This one works in darkness, cloud, fog, even underwater. It provides both compass direction and positional information.

Fourth, olfactory cues — scent. Salmon find their birth stream by its unique chemical signature. Seabirds may use their colony's smell to home in from the ocean.

Here's the key insight for the exam. Most long-distance navigators don't rely on just one system — they use redundant, overlapping navigation cues. If one fails, another takes over. You saw this in the titi experiment: block the magnetic sense alone and the birds still home using celestial cues. Block celestial cues alone and they still home using magnetic. But block both together and they're lost. That redundancy is adaptive — it's been favoured by natural selection because navigation failure during migration means death.
""",

    # 9. Migration — what it is and why it happens
    "week5_migration_intro": """
Migration. Let's make sure you've got the definition rock solid, because students lose marks here every year.

Migration is a seasonal or periodic movement between two distinct habitats, with a return journey. It's large-scale — hundreds to thousands of kilometres. It's predictable — usually tied to seasons. And it's a population-level pattern — most or all individuals migrate, not just a few.

Here's what migration is NOT. Dispersal is one-way — a juvenile bird leaving its parents' territory and never coming back. That's not migration. Nomadism is unpredictable wandering following patchy resources. That's not migration either. Migration requires a regular, return journey between defined areas.

Now, why would an animal do something so dangerous and expensive? Think of it as a cost-benefit analysis. The benefits include access to seasonal food abundance — like the Arctic summer insect bloom — better breeding habitat with fewer predators, favourable climate, and reduced parasite loads. The costs are enormous: massive energy expenditure, predation risk during transit, navigation errors that can be fatal, and missed reproduction if you arrive late.

Migration is maintained by natural selection because, on average, individuals that migrate leave more offspring than those that don't. The benefits outweigh the costs — but only just. That's why migration is always a finely balanced equation, and why even small environmental changes can tip the balance.
""",

    # 10. NZ Migration Showcase — the five species
    "week5_nz_showcase": """
Let me bring the five New Zealand migratory species to life for you.

Kuaka — the bar-tailed godwit. The undisputed champion of endurance flight. Every autumn these birds leave New Zealand estuaries and fly approximately twelve thousand kilometres non-stop to Alaska. Eight to nine days in the air. No food, no water, no rest. They navigate using sun and magnetic compasses. In 2007, a tracked female called E7 flew eleven thousand six hundred and ninety kilometres and arrived having lost half her body mass. You'll learn the physiology behind this in Week 6.

Tuna — the longfin eel. After twenty to a hundred years quietly living in a New Zealand river, adults undergo a dramatic metamorphosis — enlarged eyes, silvered skin — and migrate roughly three thousand kilometres to deep ocean trenches near Tonga to spawn and die. It's a one-way trip. This is catadromous migration — freshwater to sea to breed. The opposite of salmon, which are anadromous.

Titi — the sooty shearwater. These birds fly a sixty-five thousand kilometre figure-eight loop around the entire Pacific every year. Two hundred days at sea. They use celestial, magnetic, and olfactory navigation together — the multi-cue system you studied in Lesson 2. And Ngai Tahu muttonbirders have been recording their arrival and departure times for centuries, with observations that match modern satellite data almost exactly.

Tohora — the humpback whale. About five thousand kilometres each way between Antarctic feeding grounds and tropical breeding waters near Tonga. They fast the entire migration, living off blubber reserves. The warm tropical waters have almost no food — but they're safer for newborn calves.

And pekapeka — the short-tailed bat. New Zealand's only surviving native land mammal. These do short altitudinal migration — maybe ten to fifty kilometres — between higher elevations in summer and lower valleys in winter. They use torpor to survive the cold. They're nationally vulnerable, mainly threatened by introduced predators like rats and stoats.
""",
}


def generate_audio():
    """Generate MP3 files for all narrations. Skips files that already exist."""
    client = ElevenLabs(api_key=API_KEY)
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for name, text in NARRATIONS.items():
        output_path = os.path.join(OUTPUT_DIR, f"{name}.mp3")

        # Skip if already generated
        if os.path.exists(output_path):
            print(f"  Skipping {name} (already exists)")
            continue

        print(f"  Generating {name}...")
        audio = client.text_to_speech.convert(
            voice_id=VOICE_ID,
            text=text.strip(),
            model_id=MODEL_ID,
        )

        with open(output_path, "wb") as f:
            for chunk in audio:
                f.write(chunk)

        print(f"  ✓ Saved {output_path}")
        time.sleep(1)  # Be nice to the API


if __name__ == "__main__":
    generate_audio()
