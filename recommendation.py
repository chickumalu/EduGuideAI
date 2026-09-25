def recommend_career(answers):

    # Convert answers to lowercase
    answers = {
        key: str(value).lower().strip()
        for key, value in answers.items()
    }

    # ---------------------------------------------------------
    # CAREER PROFILES
    # ---------------------------------------------------------

    careers = {

        "Software Engineer": {
            "interest_area": ["technology"],
            "subjects": ["mathematics", "computer science", "ai"],
            "problems": ["technical problems", "mathematical problems"],
            "technology": ["very comfortable", "comfortable"],
            "calculations": ["very comfortable", "comfortable"],
            "work_type": ["office and computer work"],
            "work_style": ["practical work", "both"],
            "creativity": ["very creative", "creative"],
            "motivation": [
                "solving difficult problems",
                "creating new things",
                "learning new things"
            ]
        },

        "Data Analyst": {
            "interest_area": ["technology", "business", "science"],
            "subjects": ["mathematics", "computer science", "ai", "economics"],
            "problems": ["mathematical problems", "business problems"],
            "technology": ["very comfortable", "comfortable"],
            "calculations": ["very comfortable", "comfortable"],
            "work_type": ["research and analysis", "office and computer work"],
            "work_style": ["theoretical work", "both"],
            "motivation": [
                "solving difficult problems",
                "learning new things"
            ]
        },

        "AI / Machine Learning Engineer": {
            "interest_area": ["technology", "science"],
            "subjects": ["ai", "mathematics", "computer science", "physics"],
            "problems": ["technical problems", "mathematical problems"],
            "technology": ["very comfortable"],
            "calculations": ["very comfortable"],
            "work_type": ["office and computer work", "research and analysis"],
            "work_style": ["theoretical work", "both"],
            "motivation": [
                "solving difficult problems",
                "creating new things",
                "learning new things"
            ]
        },

        "Cybersecurity Professional": {
            "interest_area": ["technology"],
            "subjects": ["computer science", "ai", "mathematics"],
            "problems": ["technical problems", "mathematical problems"],
            "technology": ["very comfortable"],
            "calculations": ["comfortable", "very comfortable"],
            "work_type": ["office and computer work", "research and analysis"],
            "work_style": ["practical work", "both"],
            "environment": ["quiet and focused", "structured and organized"],
            "motivation": ["solving difficult problems", "learning new things"]
        },

        "Mechanical Engineer": {
            "interest_area": ["technology", "science"],
            "subjects": ["physics", "mathematics", "chemistry"],
            "problems": ["technical problems", "mathematical problems"],
            "calculations": ["very comfortable", "comfortable"],
            "technology": ["very comfortable", "comfortable"],
            "work_type": ["working with machines"],
            "work_style": ["practical work", "both"],
            "teamwork": ["mostly in a team", "both"],
            "motivation": ["solving difficult problems", "creating new things"]
        },

        "Civil Engineer": {
            "interest_area": ["technology", "science"],
            "subjects": ["mathematics", "physics", "geography"],
            "problems": [
                "technical problems",
                "mathematical problems",
                "organizational problems"
            ],
            "calculations": ["very comfortable", "comfortable"],
            "technology": ["comfortable", "very comfortable"],
            "work_type": ["outdoor work", "working with machines"],
            "work_style": ["practical work", "both"],
            "teamwork": ["mostly in a team", "both"],
            "motivation": ["solving difficult problems", "creating new things"]
        },

        "Electrical Engineer": {
            "interest_area": ["technology", "science"],
            "subjects": ["physics", "mathematics", "computer science"],
            "problems": ["technical problems", "mathematical problems"],
            "calculations": ["very comfortable", "comfortable"],
            "technology": ["very comfortable", "comfortable"],
            "work_type": ["working with machines", "research and analysis"],
            "work_style": ["practical work", "both"],
            "motivation": ["solving difficult problems", "creating new things"]
        },

        "Scientist": {
            "interest_area": ["science"],
            "subjects": ["physics", "chemistry", "biology", "mathematics", "ai"],
            "problems": ["scientific problems", "mathematical problems"],
            "calculations": ["very comfortable", "comfortable"],
            "work_type": ["research and analysis"],
            "work_style": ["theoretical work", "both"],
            "motivation": [
                "solving difficult problems",
                "learning new things",
                "creating new things"
            ]
        },

        "Chemist": {
            "interest_area": ["science"],
            "subjects": ["chemistry", "physics", "biology"],
            "problems": ["scientific problems"],
            "calculations": ["comfortable", "very comfortable"],
            "work_type": ["research and analysis"],
            "work_style": ["theoretical work", "both"],
            "motivation": [
                "solving difficult problems",
                "learning new things",
                "creating new things"
            ]
        },

        "Doctor / Healthcare Professional": {
            "interest_area": ["healthcare", "science"],
            "subjects": ["biology", "chemistry", "psychology"],
            "problems": ["scientific problems", "people-related problems"],
            "people": ["very comfortable", "comfortable"],
            "helping": ["i really enjoy it", "i enjoy it"],
            "work_type": ["working with people"],
            "priority": ["helping people", "job security"],
            "motivation": ["helping people", "making a difference"]
        },

        "Psychologist": {
            "interest_area": ["healthcare", "education"],
            "subjects": ["psychology", "biology", "english"],
            "problems": ["people-related problems"],
            "people": ["very comfortable", "comfortable"],
            "helping": ["i really enjoy it", "i enjoy it"],
            "work_type": ["working with people"],
            "teamwork": ["mostly alone", "both"],
            "priority": ["helping people", "learning and growth"],
            "motivation": ["helping people", "making a difference"]
        },

        "Environmental Scientist": {
            "interest_area": ["science"],
            "subjects": ["biology", "chemistry", "geography", "physics"],
            "problems": ["scientific problems"],
            "work_type": ["outdoor work", "research and analysis"],
            "work_style": ["practical work", "both"],
            "priority": ["learning and growth", "making a difference"],
            "motivation": ["learning new things", "making a difference"]
        },

        "Nutritionist / Dietitian": {
            "interest_area": ["healthcare", "science"],
            "subjects": ["biology", "chemistry", "psychology"],
            "problems": ["scientific problems", "people-related problems"],
            "people": ["comfortable", "very comfortable"],
            "helping": ["i really enjoy it", "i enjoy it"],
            "work_type": ["working with people"],
            "priority": ["helping people", "job security"],
            "motivation": ["helping people", "making a difference"]
        },

        "Civil Services / Government Officer": {
            "interest_area": ["law and government"],
            "subjects": ["politics", "history", "geography", "economics", "languages"],
            "problems": ["organizational problems", "people-related problems"],
            "people": ["very comfortable", "comfortable"],
            "public_speaking": ["very comfortable", "comfortable"],
            "decisions": ["very comfortable", "comfortable"],
            "work_type": ["working with people", "office and computer work"],
            "teamwork": ["mostly in a team", "both"],
            "priority": ["job security", "helping people"],
            "motivation": ["making a difference", "getting recognition"]
        },

        "Lawyer": {
            "interest_area": ["law and government"],
            "subjects": ["politics", "history", "english", "languages", "economics"],
            "problems": ["people-related problems", "organizational problems"],
            "people": ["very comfortable", "comfortable"],
            "public_speaking": ["very comfortable", "comfortable"],
            "decisions": ["very comfortable", "comfortable"],
            "work_type": ["working with people"],
            "motivation": ["getting recognition", "making a difference"]
        },

        "Defence Officer": {
            "interest_area": ["defence"],
            "subjects": ["physics", "mathematics", "geography"],
            "problems": ["technical problems", "organizational problems"],
            "calculations": ["comfortable", "very comfortable"],
            "people": ["comfortable", "very comfortable"],
            "decisions": ["very comfortable", "comfortable"],
            "work_type": ["outdoor work", "working with machines"],
            "teamwork": ["mostly in a team"],
            "environment": ["fast-paced", "structured and organized"],
            "motivation": ["making a difference", "solving difficult problems"]
        },

        "Navy Officer": {
            "interest_area": ["defence"],
            "subjects": ["physics", "mathematics", "geography"],
            "problems": ["technical problems", "organizational problems"],
            "calculations": ["very comfortable", "comfortable"],
            "work_type": ["outdoor work", "working with machines"],
            "work_style": ["practical work"],
            "teamwork": ["mostly in a team"],
            "environment": ["structured and organized", "fast-paced"],
            "motivation": ["making a difference", "solving difficult problems"]
        },

        "Police Officer": {
            "interest_area": ["law and government", "defence"],
            "subjects": ["politics", "history", "geography"],
            "problems": ["people-related problems", "organizational problems"],
            "people": ["very comfortable", "comfortable"],
            "decisions": ["very comfortable", "comfortable"],
            "work_type": ["outdoor work", "working with people"],
            "teamwork": ["mostly in a team"],
            "environment": ["fast-paced", "structured and organized"],
            "motivation": ["helping people", "making a difference"]
        },

        "Business Manager": {
            "interest_area": ["business"],
            "subjects": ["economics", "mathematics", "politics"],
            "problems": ["business problems", "organizational problems"],
            "people": ["very comfortable", "comfortable"],
            "public_speaking": ["very comfortable", "comfortable"],
            "work_type": ["working with people", "office and computer work"],
            "teamwork": ["mostly in a team", "both"],
            "decisions": ["very comfortable", "comfortable"],
            "environment": ["fast-paced", "social and active"],
            "priority": ["high income", "learning and growth"],
            "motivation": ["earning money", "getting recognition"]
        },

        "Entrepreneur": {
            "interest_area": ["business"],
            "subjects": ["economics", "mathematics"],
            "problems": ["business problems", "organizational problems"],
            "people": ["very comfortable", "comfortable"],
            "public_speaking": ["very comfortable", "comfortable"],
            "creativity": ["very creative", "creative"],
            "decisions": ["very comfortable", "comfortable"],
            "work_type": ["working with people", "office and computer work"],
            "environment": ["fast-paced", "flexible and creative"],
            "priority": ["high income", "freedom and flexibility"],
            "motivation": ["earning money", "creating new things"]
        },

        "Economist": {
            "interest_area": ["business", "science"],
            "subjects": ["economics", "mathematics", "politics"],
            "problems": ["mathematical problems", "business problems"],
            "calculations": ["very comfortable", "comfortable"],
            "work_type": ["research and analysis"],
            "work_style": ["theoretical work", "both"],
            "priority": ["learning and growth", "high income"],
            "motivation": ["solving difficult problems", "learning new things"]
        },

        "Financial Analyst": {
            "interest_area": ["business"],
            "subjects": ["mathematics", "economics"],
            "problems": ["mathematical problems", "business problems"],
            "calculations": ["very comfortable"],
            "work_type": ["research and analysis", "office and computer work"],
            "work_style": ["theoretical work", "both"],
            "priority": ["high income", "learning and growth"],
            "motivation": ["solving difficult problems", "earning money"]
        },

        "Teacher": {
            "interest_area": ["education"],
            "subjects": [
                "english",
                "mathematics",
                "languages",
                "history",
                "geography",
                "psychology",
                "physics",
                "chemistry",
                "biology",
                "computer science"
            ],
            "problems": ["people-related problems", "organizational problems"],
            "people": ["very comfortable", "comfortable"],
            "public_speaking": ["very comfortable", "comfortable"],
            "helping": ["i really enjoy it", "i enjoy it"],
            "work_type": ["working with people"],
            "teamwork": ["mostly in a team", "both"],
            "priority": ["helping people", "job security"],
            "motivation": ["helping people", "making a difference"]
        },

        "Social Worker": {
            "interest_area": ["education", "healthcare", "law and government"],
            "subjects": ["psychology", "history", "politics", "languages"],
            "problems": ["people-related problems"],
            "people": ["very comfortable"],
            "helping": ["i really enjoy it"],
            "work_type": ["working with people"],
            "teamwork": ["mostly in a team", "both"],
            "priority": ["helping people"],
            "motivation": ["helping people", "making a difference"]
        },

        "Counsellor": {
            "interest_area": ["education", "healthcare"],
            "subjects": ["psychology", "english", "languages"],
            "problems": ["people-related problems"],
            "people": ["very comfortable"],
            "public_speaking": ["comfortable", "very comfortable"],
            "helping": ["i really enjoy it", "i enjoy it"],
            "work_type": ["working with people"],
            "priority": ["helping people"],
            "motivation": ["helping people", "making a difference"]
        },

        "Journalist": {
            "interest_area": ["media and communication"],
            "subjects": ["english", "languages", "history", "politics"],
            "problems": ["people-related problems", "creative problems"],
            "people": ["very comfortable", "comfortable"],
            "public_speaking": ["very comfortable", "comfortable"],
            "work_type": ["working with people", "creative work"],
            "environment": ["fast-paced", "social and active"],
            "motivation": ["getting recognition", "making a difference"]
        },

        "Media Professional": {
            "interest_area": ["media and communication"],
            "subjects": ["english", "languages", "multimedia"],
            "problems": ["creative problems", "people-related problems"],
            "creativity": ["very creative", "creative"],
            "people": ["very comfortable", "comfortable"],
            "public_speaking": ["very comfortable", "comfortable"],
            "work_type": ["creative work", "working with people"],
            "environment": ["social and active", "fast-paced"],
            "motivation": ["creating new things", "getting recognition"]
        },

        "Graphic Designer": {
            "interest_area": ["arts and creativity", "beauty and fashion"],
            "subjects": ["multimedia", "english"],
            "problems": ["creative problems"],
            "creativity": ["very creative", "creative"],
            "technology": ["comfortable", "very comfortable"],
            "work_type": ["creative work"],
            "work_style": ["practical work", "both"],
            "environment": ["flexible and creative"],
            "priority": ["creativity", "freedom and flexibility"],
            "motivation": ["creating new things"]
        },

        "Artist": {
            "interest_area": ["arts and creativity"],
            "subjects": ["multimedia", "english"],
            "problems": ["creative problems"],
            "creativity": ["very creative"],
            "work_type": ["creative work"],
            "work_style": ["practical work"],
            "environment": ["flexible and creative"],
            "priority": ["creativity", "freedom and flexibility"],
            "motivation": ["creating new things"]
        },

        "Fashion Designer": {
            "interest_area": ["beauty and fashion", "arts and creativity"],
            "subjects": ["multimedia", "english"],
            "problems": ["creative problems"],
            "creativity": ["very creative", "creative"],
            "work_type": ["creative work"],
            "work_style": ["practical work"],
            "environment": ["flexible and creative"],
            "priority": ["creativity", "freedom and flexibility"],
            "motivation": ["creating new things"]
        },

        "Makeup Artist": {
            "interest_area": ["beauty and fashion", "arts and creativity"],
            "subjects": ["multimedia", "english"],
            "problems": ["creative problems"],
            "creativity": ["very creative", "creative"],
            "people": ["very comfortable", "comfortable"],
            "work_type": ["creative work", "working with people"],
            "work_style": ["practical work"],
            "environment": ["flexible and creative"],
            "priority": ["creativity", "freedom and flexibility"],
            "motivation": ["creating new things"]
        },

        "Beauty & Skincare Professional": {
            "interest_area": ["beauty and fashion", "healthcare"],
            "subjects": ["biology", "chemistry"],
            "problems": ["scientific problems", "people-related problems"],
            "people": ["very comfortable", "comfortable"],
            "helping": ["i really enjoy it", "i enjoy it"],
            "work_type": ["working with people"],
            "work_style": ["practical work"],
            "priority": ["helping people", "freedom and flexibility"],
            "motivation": ["helping people", "creating new things"]
        },

        "Photographer": {
            "interest_area": ["arts and creativity", "media and communication"],
            "subjects": ["multimedia", "english"],
            "problems": ["creative problems"],
            "creativity": ["very creative", "creative"],
            "technology": ["comfortable", "very comfortable"],
            "work_type": ["creative work", "outdoor work"],
            "work_style": ["practical work"],
            "environment": ["flexible and creative", "social and active"],
            "priority": ["creativity", "freedom and flexibility"],
            "motivation": ["creating new things"]
        },

        "Sports Coach": {
            "interest_area": ["sports"],
            "subjects": ["biology", "physics"],
            "problems": ["people-related problems", "organizational problems"],
            "people": ["very comfortable", "comfortable"],
            "public_speaking": ["comfortable", "very comfortable"],
            "helping": ["i really enjoy it", "i enjoy it"],
            "work_type": ["outdoor work", "working with people"],
            "teamwork": ["mostly in a team"],
            "environment": ["social and active", "fast-paced"],
            "priority": ["helping people", "learning and growth"],
            "motivation": ["helping people", "making a difference"]
        },

        "Professional Athlete": {
            "interest_area": ["sports"],
            "subjects": ["biology", "physics"],
            "problems": ["technical problems"],
            "work_type": ["outdoor work"],
            "work_style": ["practical work"],
            "teamwork": ["mostly in a team", "both"],
            "environment": ["fast-paced", "social and active"],
            "priority": ["freedom and flexibility", "high income"],
            "motivation": ["getting recognition", "solving difficult problems"]
        },

        "Air Hostess / Cabin Crew": {
            "interest_area": ["aviation"],
            "subjects": ["english", "languages", "geography"],
            "problems": ["people-related problems", "organizational problems"],
            "people": ["very comfortable"],
            "public_speaking": ["very comfortable", "comfortable"],
            "helping": ["i enjoy it", "i really enjoy it"],
            "work_type": ["working with people"],
            "teamwork": ["mostly in a team"],
            "environment": ["fast-paced", "social and active"],
            "priority": ["freedom and flexibility", "learning and growth"],
            "motivation": ["helping people", "making a difference"]
        },

        "Historian": {
            "interest_area": ["education", "law and government", "media and communication"],
            "subjects": ["history", "politics", "english", "languages"],
            "problems": ["organizational problems", "people-related problems"],
            "work_type": ["research and analysis"],
            "work_style": ["theoretical work", "both"],
            "teamwork": ["mostly alone", "both"],
            "priority": ["learning and growth"],
            "motivation": ["learning new things", "making a difference"]
        },

        "Geographer": {
            "interest_area": ["science", "education"],
            "subjects": ["geography", "mathematics", "physics", "history"],
            "problems": ["scientific problems", "organizational problems"],
            "calculations": ["comfortable", "very comfortable"],
            "work_type": ["outdoor work", "research and analysis"],
            "work_style": ["practical work", "theoretical work", "both"],
            "priority": ["learning and growth"],
            "motivation": ["learning new things", "solving difficult problems"]
        }
    }


    # ---------------------------------------------------------
    # QUESTION WEIGHTS
    # ---------------------------------------------------------

    weights = {

        "interest_area": 6,
        "interest_subject": 5,
        "highest_subject": 5,
        "easy_subject": 3,

        "problems": 4,

        "calculations": 3,
        "technology": 3,
        "people": 3,
        "public_speaking": 2,
        "creativity": 3,
        "helping": 3,

        "work_type": 4,
        "work_style": 2,
        "teamwork": 2,
        "decisions": 2,
        "environment": 2,

        "priority": 3,
        "motivation": 3
    }


    # ---------------------------------------------------------
    # INITIALIZE SCORES
    # ---------------------------------------------------------

    scores = {
        career: 0
        for career in careers
    }


    # ---------------------------------------------------------
    # MATCH ANSWERS TO CAREER PROFILES
    # ---------------------------------------------------------

    for career, profile in careers.items():

        for question, suitable_answers in profile.items():

            # Subjects are special because the student can
            # type any subject.
            if question == "subjects":

                subject_questions = [
                    "interest_subject",
                    "easy_subject",
                    "highest_subject"
                ]

                for subject_question in subject_questions:

                    student_subject = answers.get(
                        subject_question,
                        ""
                    )

                    if student_subject in suitable_answers:

                        if subject_question == "interest_subject":
                            scores[career] += 5

                        elif subject_question == "highest_subject":
                            scores[career] += 5

                        else:
                            scores[career] += 3

                continue


            # Normal multiple-choice questions
            student_answer = answers.get(
                question,
                ""
            )

            if student_answer in suitable_answers:

                scores[career] += weights.get(
                    question,
                    1
                )


    # ---------------------------------------------------------
    # TEXT ANSWER KEYWORDS
    # ---------------------------------------------------------

    text_fields = [
        "talent",
        "good_at",
        "talk_about",
        "activity"
    ]


    keywords = {

        "Software Engineer": [
            "coding", "programming", "computer",
            "software", "technology", "ai", "robot"
        ],

        "Data Analyst": [
            "data", "analysis", "numbers",
            "statistics", "mathematics", "research"
        ],

        "AI / Machine Learning Engineer": [
            "ai", "artificial intelligence",
            "machine learning", "coding",
            "programming", "technology"
        ],

        "Cybersecurity Professional": [
            "cybersecurity", "security", "hacking",
            "computer", "technology", "network"
        ],

        "Mechanical Engineer": [
            "machine", "machines", "mechanical",
            "engineering", "robot", "physics"
        ],

        "Civil Engineer": [
            "construction", "building", "structures",
            "roads", "engineering", "architecture"
        ],

        "Electrical Engineer": [
            "electricity", "electrical", "electronics",
            "circuits", "engineering", "technology"
        ],

        "Scientist": [
            "science", "research", "experiment",
            "physics", "chemistry", "biology"
        ],

        "Chemist": [
            "chemistry", "chemical", "laboratory",
            "lab", "experiment"
        ],

        "Doctor / Healthcare Professional": [
            "doctor", "medicine", "health",
            "medical", "patient", "biology"
        ],

        "Psychologist": [
            "psychology", "behavior", "people",
            "counselling", "mental", "helping"
        ],

        "Environmental Scientist": [
            "environment", "climate", "nature",
            "pollution", "earth", "research"
        ],

        "Nutritionist / Dietitian": [
            "nutrition", "food", "diet",
            "health", "fitness", "biology"
        ],

        "Civil Services / Government Officer": [
            "government", "administration",
            "public service", "politics",
            "leadership", "society"
        ],

        "Lawyer": [
            "law", "debate", "argument",
            "justice", "rights", "politics"
        ],

        "Defence Officer": [
            "defence", "army", "military",
            "leadership", "discipline", "security"
        ],

        "Navy Officer": [
            "navy", "sea", "ship",
            "marine", "military", "defence"
        ],

        "Police Officer": [
            "police", "crime", "law",
            "security", "justice", "investigation"
        ],

        "Business Manager": [
            "business", "leadership",
            "management", "money", "manager"
        ],

        "Entrepreneur": [
            "business", "startup",
            "entrepreneur", "leadership",
            "money", "innovation"
        ],

        "Economist": [
            "economics", "economy",
            "markets", "finance", "money"
        ],

        "Financial Analyst": [
            "finance", "financial",
            "stocks", "investment", "numbers",
            "money", "analysis"
        ],

        "Teacher": [
            "teaching", "teacher",
            "explaining", "education", "students"
        ],

        "Social Worker": [
            "social work", "helping",
            "community", "people", "society"
        ],

        "Counsellor": [
            "counselling", "counseling",
            "psychology", "helping",
            "listening", "people"
        ],

        "Journalist": [
            "journalism", "news",
            "writing", "reporting", "media"
        ],

        "Media Professional": [
            "media", "video", "content",
            "communication", "film", "television"
        ],

        "Graphic Designer": [
            "design", "drawing", "graphics",
            "art", "creative", "multimedia"
        ],

        "Artist": [
            "art", "drawing", "painting",
            "sketching", "creative"
        ],

        "Fashion Designer": [
            "fashion", "clothes", "design",
            "style", "textile"
        ],

        "Makeup Artist": [
            "makeup", "make up", "beauty",
            "cosmetics", "styling"
        ],

        "Beauty & Skincare Professional": [
            "skincare", "skin", "beauty",
            "cosmetics", "facial", "makeup"
        ],

        "Photographer": [
            "photography", "photographer",
            "camera", "photos", "pictures"
        ],

        "Sports Coach": [
            "coach", "coaching", "sports",
            "training", "fitness", "athlete"
        ],

        "Professional Athlete": [
            "sports", "athlete", "football",
            "cricket", "basketball", "running"
        ],

        "Air Hostess / Cabin Crew": [
            "aviation", "airline", "flight",
            "travel", "cabin crew"
        ],

        "Historian": [
            "history", "historical",
            "past", "culture", "ancient"
        ],

        "Geographer": [
            "geography", "maps", "mapping",
            "climate", "earth", "environment"
        ]
    }


    # Add small bonuses for useful text matches
    for field in text_fields:

        text = answers.get(field, "")

        for career, career_keywords in keywords.items():

            for keyword in career_keywords:

                if keyword in text:

                    scores[career] += 2


    # ---------------------------------------------------------
    # FINAL RECOMMENDATION
    # ---------------------------------------------------------

    recommended_career = max(
        scores,
        key=scores.get
    )

    return recommended_career
