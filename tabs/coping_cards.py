import streamlit as st

def show_coping_cards():
    st.header("🧘‍♀️ Coping Strategies & Wellness Tools")
    st.write("Evidence-based techniques to help you manage stress, anxiety, and difficult emotions. Click on any card to learn more.")
    
    # Create filter boxes using columns
    st.subheader("Choose a Category:")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    # col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    
    with col1:
        if st.button("🌟 All Techniques", use_container_width=True):
            st.session_state.selected_category = "All"
    
    with col2:
        if st.button("😰 Anxiety & Panic", use_container_width=True):
            st.session_state.selected_category = "Anxiety & Panic"
    
    with col3:
        if st.button("😴 Sleep & Relaxation", use_container_width=True):
            st.session_state.selected_category = "Sleep & Relaxation"
    
    with col4:
        if st.button("🧠 Mindfulness & Awareness", use_container_width=True):
            st.session_state.selected_category = "Mindfulness"
    
    with col5:
        if st.button("💪 Quick Relief & Support", use_container_width=True):
            st.session_state.selected_category = "Quick Relief"
    
    # Initialize session state if not exists
    if 'selected_category' not in st.session_state:
        st.session_state.selected_category = "All"
    
    # Display cards based on selection
    st.markdown("---")
    st.subheader(f"Category: {st.session_state.selected_category}")
    
    if st.session_state.selected_category == "All":
        show_all_cards()
    else:
        show_category_cards(st.session_state.selected_category)

def get_coping_cards_data():
    """Return hardcoded coping cards data"""
    return [
        # Anxiety & Panic techniques
        {
            "category": "Anxiety & Panic",
            "title": "Deep Breathing (4-7-8)",
            "description": """**What it helps:** Acute anxiety, panic attacks, calming before sleep

**How to do it:**
1. Inhale through nose for 4 counts
2. Hold breath for 7 counts
3. Exhale through mouth for 8 counts
4. Repeat 3-4 cycles

**When to use:** 1-3 times daily, during anxiety episodes

**Safety:** Stop if you feel dizzy or lightheaded"""
        },
        {
            "category": "Anxiety & Panic", 
            "title": "5-4-3-2-1 Grounding",
            "description": """**What it helps:** Overwhelming anxiety, panic, brings you to the present

**How to do it:**
1. Take 2-3 slow breaths
2. **See** 5 things around you
3. **Touch** 4 different textures
4. **Hear** 3 sounds
5. **Smell** 2 scents
6. **Taste** 1 thing

**When to use:** During panic attacks, overwhelming emotions

**Tip:** Practice when calm so it's easier during crisis"""
        },
        
        # Quick Relief techniques
        {
            "category": "Quick Relief",
            "title": "TIPP Technique",
            "description": """**What it helps:** Urgent emotional crises, severe distress

**T - Temperature:** Splash cold water on face or hold ice for 30 seconds
**I - Intense Exercise:** 30-60 seconds of jumping jacks or running in place
**P - Paced Breathing:** Slow breathing (inhale 4, exhale 6) for 2 minutes
**P - Progressive Relaxation:** Tense and relax muscle groups

**When to use:** During emotional crisis (use for 10-15 minutes)

**Safety:** Stop intense exercise if chest pain or dizziness occurs"""
        },
        {
            "category": "Quick Relief",
            "title": "Opposite Action",
            "description": """**What it helps:** Managing difficult emotions, breaking negative cycles

**How it works:** Do the opposite of what your emotion tells you to do

**Examples:**
• **Anger** → Instead of yelling, speak quietly and politely
• **Sadness** → Instead of withdrawing, call or visit a friend
• **Anxiety** → Instead of avoiding, do something engaging

**When to use:** When emotions feel overwhelming or unhelpful

**Tip:** May feel forced at first, but can shift emotions positively"""
        },
        {
            "category": "Quick Relief",
            "title": "Self-Soothing with 5 Senses",
            "description": """**What it helps:** Immediate comfort during distress

**How to use:**
• **See:** Look at calming pictures, nature, soft lighting
• **Hear:** Listen to favorite music, nature sounds, calming playlist
• **Touch:** Hold soft blanket, stress ball, warm cup
• **Smell:** Use pleasant scents, essential oils, flowers
• **Taste:** Sip herbal tea, eat mindfully, taste something soothing

**When to use:** During distress episodes, as part of 'distress box'

**Tip:** Prepare items in advance for quick access"""
        },
        
        # Sleep & Relaxation techniques
        {
            "category": "Sleep & Relaxation",
            "title": "Progressive Muscle Relaxation",
            "description": """**What it helps:** Tension, anxiety, trouble sleeping

**How to do it:**
1. Lie down comfortably
2. Start with feet - tense for 5-7 seconds, then relax for 20-30 seconds
3. Move through: calves → thighs → abdomen → chest → hands → arms → shoulders → face
4. Notice the difference between tension and relaxation

**When to use:** Daily, especially before bed

**Tip:** Breathe in while tensing, out while relaxing"""
        },
        {
            "category": "Sleep & Relaxation",
            "title": "Sleep Hygiene Guide",
            "description": """**What it helps:** Difficulty falling asleep, poor sleep quality

**Key strategies:**
• Fixed sleep/wake times (even weekends)
• Wind down 30-60 minutes before bed
• No caffeine after early afternoon
• Bedroom only for sleep
• Get morning sunlight (10-30 minutes)
• Cool, dark, quiet room

**If you can't sleep:** Get up after 15-20 minutes, do quiet activity, return when sleepy

**Safety:** See doctor if insomnia lasts >3 weeks"""
        },
        {
            "category": "Sleep & Relaxation",
            "title": "Aromatherapy Basics",
            "description": """**What it helps:** Mild anxiety, sleep difficulties, relaxation

**Safe uses:**
• **Diffuser:** 3-5 drops lavender oil, run 15-30 minutes before bed
• **Inhaler:** 1 drop on tissue, inhale gently
• **Bath:** 2-3 drops in carrier oil, add to bath

**Common oils:** Lavender (sleep/calming), bergamot (mood lift), peppermint (alertness)

**Safety:** Never ingest oils, patch-test on skin, keep away from children and pets"""
        },
        
        # Mindfulness techniques
        {
            "category": "Mindfulness",
            "title": "Mindful Breathing Meditation",
            "description": """**What it helps:** Stress, rumination, persistent worry

**How to do it:**
1. Sit comfortably, set timer for 5-10 minutes
2. Close eyes, take 3 slow breaths
3. Focus on breath at nostrils or belly
4. When thoughts come, gently label 'thinking' and return to breath
5. No judgment if mind wanders

**When to use:** Daily, start with 5 minutes

**Safety:** Stop if panic or traumatic memories increase"""
        },
        {
            "category": "Mindfulness",
            "title": "Falling Leaves Technique",
            "description": """**What it helps:** Letting go of worries, rumination, preparing for sleep

**How to do it:**
1. Sit comfortably, close eyes, take 3 slow breaths
2. Imagine a quiet tree in a park
3. Picture each worry as a leaf on the tree
4. As you breathe out, watch the leaf fall and float away
5. Repeat with each worry
6. Feel yourself becoming lighter

**When to use:** Daily or when ruminating, before sleep"""
        },
        {
            "category": "Mindfulness",
            "title": "Gratitude Practice",
            "description": """**What it helps:** Low mood, building happiness, self-esteem

**Daily practices:**
• **Gratitude Journal:** Write 3 good things about your day each evening
• **Give Thanks:** Actively notice and thank people for good deeds
• **Mindful Walk:** Focus on appreciating your surroundings
• **Grateful Contemplation:** Spend 5-10 minutes reviewing good things from your day

**When to use:** Daily as part of self-care routine

**Tip:** Focus on small things - a good meal, talking to a friend"""
        }
    ]

def show_all_cards():
    """Display all coping cards"""
    cards = get_coping_cards_data()
    display_cards(cards)

def show_category_cards(category):
    """Display cards for a specific category"""
    cards = get_coping_cards_data()
    filtered_cards = [card for card in cards if card["category"] == category]
    
    if filtered_cards:
        display_cards(filtered_cards)
    else:
        st.info(f"No cards found in the {category} category.")

def display_cards(cards):
    """Display cards in a grid layout"""
    if not cards:
        st.info("No coping cards available.")
        return
    
    # Create grid layout - 2 cards per row
    for i in range(0, len(cards), 2):
        cols = st.columns(2)
        
        # Display first card in row
        with cols[0]:
            card = cards[i]
            with st.expander(f"📝 {card['title']}", expanded=False):
                st.markdown(f"**Category:** {card['category']}")
                st.markdown("---")
                st.markdown(card['description'])
                
                if st.button(f"✅ I tried this technique", key=f"tried_{i}"):
                    st.success("Great job trying this technique! Remember, practice makes it more effective.")
        
        # Display second card in row if it exists
        if i + 1 < len(cards):
            with cols[1]:
                card = cards[i + 1]
                with st.expander(f"📝 {card['title']}", expanded=False):
                    st.markdown(f"**Category:** {card['category']}")
                    st.markdown("---")
                    st.markdown(card['description'])
                    
                    if st.button(f"✅ I tried this technique", key=f"tried_{i+1}"):
                        st.success("Great job trying this technique! Remember, practice makes it more effective.")
        
        # Add space between rows
        st.markdown("<br>", unsafe_allow_html=True)

# if __name__ == "__main__":
#     show_coping_cards()