import json

resume_content = {
    "name": "Alok Prasad",
    "contact_info": {
        "location": "Chennai, Tamil Nadu, India",
        "phone": "8887685835",
        "email": "prasadalok705@gmail.com",
        "linkedin": "linkedin.com/in/alok705",
        "portfolio": "portfolio.techyalok.com"
    },
    "technical_skills": {
        "languages": ["C", "C++", "Java", "Kotlin"],
        "developer_tools": ["Arduino IDE", "Android Studio", "IntelliJ IDEA", "Git/Github"],
        "technologies": ["App Dev.", "Embedded System", "Internet of Things", "Linux"],
        "soft_skills": ["Problem Solving", "Self-learning", "Adaptability", "Time management", "Leadership", "Multi-tasking"]
    },
    "education": {
        "institution": "SRM Institute of Science and Technology",
        "degree": "Bachelor of Technology in CSE",
        "GPA": "9.15"
    },
    "experience": [
        {
            "title": "Android Development Intern",
            "company": "CodeClause",
            "duration": "Sep 2023 - Oct 2023",
            "location": "Chennai, Tamil Nadu",
            "description": [
                "Led QRScan-Karo, a Jetpack Compose QR code app, incorporating CompoundBarcodeView for scanning and a novel media picker for image-based QR code retrieval.",
                "Mastered Kotlin, Jetpack Compose, Android view integration within composables, scanner implementation, navigation, etc.",
                "Elevated QRScan-Karo by enabling diverse functionalities: QR code generation, linkification, copy, sharing options, enhancing user experience and functionality."
            ]
        },
        {
            "title": "Former Associate, Tesla Lab and Norman Lab",
            "company": "SRM Next Tech Lab",
            "duration": "Nov 2022 - Dec 2023",
            "location": "Chennai, Tamil Nadu",
            "description": [
                "Collaborated with colleagues on IoT, App Dev, and Embedded System projects.",
                "Proactively participated in enriching seminars hosted by the Next Tech Lab, fostering continuous learning and technological awareness."
            ]
        }
    ],
    "projects": [
        {
            "name": "Smart Socket",
            "field": "Internet Of Things, Software Development, Embedded System",
            "description": [
                "Designed a Smart Socket offering two modes: offline manual control and remote control via the mobile app.",
                "Integrated Firebase for real-time data exchange between the socket and Android app.",
                "Developed firmware for NodeMCU and an Android app.",
                "Tech Stack: Kotlin, C++, Firebase, NodeMCU, Android Studio"
            ],
            "github_link": "Repository"
        },
        {
            "name": "Fire Alarm System",
            "field": "Embedded System",
            "description": [
                "Developed a responsive Arduino-based system for instant fire detection and swift response.",
                "Integrated advanced features, enabling autonomous SOS calls to the fire department via the sim800l module.",
                "Continuously improving and expanding functionality by adding new features and refining existing ones.",
                "Tech Stack: C++, Sim800l, IR Sensor, MCU: Arduino Nano"
            ]
        }
    ],
    "certifications": [
        "Oracle Cloud Infrastructure 2023 Certified Foundations Associate",
        "Programming in Java : NPTEL | By Prof. Debasis Samanta | IIT Kharagpur",
        "AICTE AWS Virtual Internship : AWS Cloud | Supported by AWS Academy"
    ],
    "achievements": [
        "Trikon Unite Hackathon : First Runner Up | Developed a robust RFID and AI-based facial recognition system to replace traditional boarding passes | April 2024",
        "CBSE Sci. Expo (2019) : Qualified at the regional CBSE Science Exhibition and was selected for the national level.",
        "Codechef : Rating: 1151 | Solved over 200+ problems",
        "HackerRank : 5 ⋆ in C++"
    ]
}

json_output = json.dumps(resume_content, indent=4)
print(json_output)
