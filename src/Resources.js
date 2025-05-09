import React, { useEffect, useState } from 'react';
import './Resources.css';

const baseUrl = process.env.REACT_APP_API_BASE;

const ResourceCard = ({ title, description, link, action }) => (
  <div className="resource-card">
    <h3>{title}</h3>
    <p>{description}</p>
    {link ? (
      <a href={link} target="_blank" rel="noopener noreferrer">View advice</a>
    ) : action ? (
      <a href="#" onClick={(e) => {
        e.preventDefault();
        action();
      }}>View advice</a>
    ) : null}
  </div>
);

const Resources = ({ setView }) => {
  const [phq9, setPhq9] = useState(null);
  const [gad7, setGad7] = useState(null);
  const [moodStreak, setMoodStreak] = useState(0);
  const [tips, setTips] = useState([]);

  const user_id = localStorage.getItem("uid");

useEffect(() => {
  if (!user_id) return;

  const token = localStorage.getItem("token");
  if (!token) {
    console.warn("No Firebase auth token found in localStorage.");
    return;
  }

  const headers = {
    "Authorization": `Bearer ${token}`
  };

  // Fetch latest assessment
  fetch(`${baseUrl}/assessment/results?user_id=${user_id}`, { headers })
    .then(res => res.json())
    .then(data => {
      if (!Array.isArray(data) || data.length === 0) return;
      const latest = data[data.length - 1];
      setPhq9(latest?.phq9 || 0);
      setGad7(latest?.gad7 || 0);
    })
    .catch(err => {
      console.error("Error fetching assessment results:", err);
    });

  // Fetch moods and calculate streak
  fetch(`${baseUrl}/mood?user_id=${user_id}`, { headers })
    .then(res => res.json())
    .then(data => {
      const streak = Array.isArray(data) ? calculateStreak(data) : 0;
      setMoodStreak(streak);
    })
    .catch(err => {
      console.error("Error fetching mood data:", err);
    });

}, [user_id]);

  useEffect(() => {
    const suggestions = [];

    if (phq9 >= 15) {
      suggestions.push({
        title: "💡 Managing Severe Depression",
        description: "Explore professional strategies and support for managing depression.",
        action: () => setView('depression')
      });
    }

    if (gad7 >= 10) {
      suggestions.push({
        title: "🧘 Grounding Techniques for Anxiety",
        description: "Step-by-step calming exercises when feeling overwhelmed.",
        action: () => setView('anxiety')
      });
    }

    if (moodStreak < 3) {
      suggestions.push({
        title: "🔁 Build Your Self-Care Streak",
        description: "Get back on track with small habits and rewards.",
      });
    }

    if (suggestions.length === 0) {
      suggestions.push({
        title: "🌱 Boost Everyday Wellbeing",
        description: "Ideas for daily positivity, study breaks and social connection.",
        action: () => setView('wellbeing')
      });
    }

    setTips(suggestions);
  }, [phq9, gad7, moodStreak]);

  // Count how many consecutive days the user logged a mood
  const calculateStreak = (entries) => {
  const dates = Array.isArray(entries)
    ? entries.map(entry => new Date(entry.timestamp).toDateString())
    : [];

  const dateSet = new Set(dates);

  let streak = 0;
  let today = new Date();

  while (true) {
    if (dateSet.has(today.toDateString())) {
      streak++;
      today.setDate(today.getDate() - 1);
    } else {
      break;
    }
  }

  return streak;
};

  const generalAdvice = [
    {
      title: "📚 Study Skills & Focus",
      description: "Time management, dealing with procrastination, and building study motivation.",
      action: () => setView('study')
    },
    {
      title: "🎤 Presentation Anxiety",
      description: "Learn how to manage performance pressure and anxiety.",
      action: () => setView('presentations')
    },
    {
      title: "🏠 Homesickness & Culture Shock",
      description: "Tips to adjust, connect and thrive while far from home.",
      action: () => setView('homesickness')
    },
    {
      title: "💸 Budgeting & Financial Stress",
      description: "Understand how to manage money and reduce financial worry.",
      action: () => setView('budgeting')
    },
    {
      title: "😴 Sleep Hygiene & Routines",
      description: "Build healthy sleep habits to support mood and energy.",
      action: () => setView('sleep')
    },
    {
      title: "🤝 Making Friends & Social Support",
      description: "Ways to overcome isolation and connect with others at uni.",
      action: () => setView('social')
    },
    {
      title: "🌍 Navigating UK Student Life",
      description: "International student guide to healthcare, culture, and survival tips.",
      action: () => setView('ukguide')
    },
    {
      title: "🆘 Crisis & Emergency Help",
      description: "What to do in a mental health crisis and who to contact.",
      action: () => setView('emergency')
    }
  ];

  return (
    <div className="resources-container">
      <h1>Personalised Wellbeing Tips</h1>
      <p>Based on your recent check-ins and assessments</p>
      <div className="resource-grid">
        {tips.map((tip, idx) => (
          <ResourceCard key={idx} {...tip} />
        ))}
      </div>

      <hr style={{ margin: '3rem 0' }} />

      <h1>General Advice for Students</h1>
      <p>Explore common challenges students face and how to manage them.</p>
      <div className="resource-grid">
        {generalAdvice.map((item, idx) => (
          <ResourceCard key={idx} {...item} />
        ))}
      </div>
    </div>
  );
};

export default Resources;
