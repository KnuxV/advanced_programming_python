---
layout: page
title: Welcome to Class - Quick Poll
---

# Welcome to Class!

Before we begin, please help us understand our class composition by answering these quick questions:

<div class="poll-container">
  <form id="pollForm">
    <div class="poll-section">
      <h3>🗣️ In which language would you prefer I teach this class?</h3>
      <div class="poll-options" id="languageOptions">
        <label class="poll-option">
          <input type="radio" name="language" value="english-okay-french">
          <span>English but I'm okay with French</span>
        </label>
        <label class="poll-option">
          <input type="radio" name="language" value="french-okay-english">
          <span>French but I'm okay with English</span>
        </label>
        <label class="poll-option">
          <input type="radio" name="language" value="english-only">
          <span>English (I'll struggle with French)</span>
        </label>
        <label class="poll-option">
          <input type="radio" name="language" value="french-only">
          <span>French (I'll struggle with English)</span>
        </label>
      </div>
    </div>

    <div class="poll-section">
      <h3>💻 What operating system do you use?</h3>
      <div class="poll-options" id="osOptions">
        <label class="poll-option">
          <input type="radio" name="os" value="windows">
          <span>Windows</span>
        </label>
        <label class="poll-option">
          <input type="radio" name="os" value="mac">
          <span>macOS</span>
        </label>
        <label class="poll-option">
          <input type="radio" name="os" value="linux">
          <span>Linux</span>
        </label>
        <label class="poll-option">
          <input type="radio" name="os" value="chromeos">
          <span>ChromeOS</span>
        </label>
        <label class="poll-option">
          <input type="radio" name="os" value="mobile">
          <span>Mobile (iOS/Android)</span>
        </label>
        <label class="poll-option">
          <input type="radio" name="os" value="other">
          <span>Other</span>
        </label>
      </div>
    </div>

    <div class="submit-section">
      <button type="submit" id="submitBtn">Submit Responses</button>
    </div>
  </form>

  <div id="results">
    <h2>Live Results</h2>
    
    <div class="poll-section">
      <h3>🗣️ Teaching Language Preference</h3>
      <div class="results" id="languageResults">
        <p style="text-align: center; color: #666; font-style: italic;">No votes yet - results will appear here as students respond!</p>
      </div>
    </div>
    
    <div class="poll-section">
      <h3>💻 Operating Systems</h3>
      <div class="results" id="osResults">
        <p style="text-align: center; color: #666; font-style: italic;">No votes yet - results will appear here as students respond!</p>
      </div>
    </div>
  </div>
</div>

<style>
.poll-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  background: white;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.poll-section {
  background: #f8f9fa;
  padding: 1.5rem;
  margin: 2rem 0;
  border-radius: 8px;
  border-left: 4px solid #3498db;
}

.poll-section h3 {
  color: #2c3e50;
  margin-top: 0;
}

.poll-options {
  display: grid;
  gap: 0.5rem;
  margin: 1rem 0;
}

.poll-option {
  display: flex;
  align-items: center;
  padding: 0.75rem;
  background: white;
  border: 2px solid #e9ecef;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s ease;
}

.poll-option:hover {
  border-color: #3498db;
  background-color: #f0f8ff;
}

.poll-option input[type="radio"] {
  margin-right: 0.75rem;
  transform: scale(1.2);
}

.poll-option.selected {
  border-color: #3498db;
  background-color: #e8f4fd;
}

.results {
  margin-top: 1rem;
  padding: 1rem;
  background: white;
  border-radius: 6px;
  border: 1px solid #dee2e6;
}

.result-bar {
  display: flex;
  align-items: center;
  margin: 0.5rem 0;
}

.result-label {
  min-width: 120px;
  font-weight: 500;
}

.result-progress {
  flex: 1;
  height: 20px;
  background: #e9ecef;
  border-radius: 10px;
  margin: 0 0.5rem;
  overflow: hidden;
}

.result-fill {
  height: 100%;
  background: linear-gradient(90deg, #3498db, #2980b9);
  border-radius: 10px;
  transition: width 0.3s ease;
}

.result-count {
  font-weight: 500;
  min-width: 60px;
  text-align: right;
}

.submit-section {
  text-align: center;
  margin-top: 2rem;
}

button {
  background: #3498db;
  color: white;
  border: none;
  padding: 0.75rem 2rem;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

button:hover {
  background: #2980b9;
}

button:disabled {
  background: #95a5a6;
  cursor: not-allowed;
}
</style>

<script>
// Store results in memory
let pollResults = {
  language: {},
  os: {}
};

document.addEventListener('DOMContentLoaded', function() {
  // Add click handlers for visual selection
  document.querySelectorAll('.poll-option').forEach(option => {
    option.addEventListener('click', function() {
      const radio = this.querySelector('input[type="radio"]');
      const group = radio.name;
      
      // Remove selected class from other options in the same group
      document.querySelectorAll(`input[name="${group}"]`).forEach(r => {
        r.closest('.poll-option').classList.remove('selected');
      });
      
      // Add selected class to this option
      this.classList.add('selected');
      radio.checked = true;
    });
  });

  // Handle form submission
  document.getElementById('pollForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const formData = new FormData(this);
    const languageChoice = formData.get('language');
    const osChoice = formData.get('os');
    
    if (!languageChoice || !osChoice) {
      alert('Please answer both questions before submitting!');
      return;
    }
    
    // Update results
    pollResults.language[languageChoice] = (pollResults.language[languageChoice] || 0) + 1;
    pollResults.os[osChoice] = (pollResults.os[osChoice] || 0) + 1;
    
    // Update live results
    displayResults();
    
    // Show thank you message and keep form visible
    alert('Thank you for your response! You can see the live results below.');
    
    // Reset form for next student
    this.reset();
    document.querySelectorAll('.poll-option').forEach(option => {
      option.classList.remove('selected');
    });
  });

  function displayResults() {
    displayCategoryResults('language', 'languageResults', {
      'english-okay-french': 'English but okay with French',
      'french-okay-english': 'French but okay with English', 
      'english-only': 'English (struggle with French)',
      'french-only': 'French (struggle with English)'
    });
    
    displayCategoryResults('os', 'osResults', {
      'windows': 'Windows',
      'mac': 'macOS',
      'linux': 'Linux', 
      'chromeos': 'ChromeOS',
      'mobile': 'Mobile',
      'other': 'Other'
    });
  }

  function displayCategoryResults(category, containerId, labels) {
    const container = document.getElementById(containerId);
    const results = pollResults[category];
    const total = Object.values(results).reduce((sum, count) => sum + count, 0);
    
    let html = '';
    
    Object.entries(labels).forEach(([key, label]) => {
      const count = results[key] || 0;
      const percentage = total > 0 ? (count / total * 100) : 0;
      
      html += `
        <div class="result-bar">
          <div class="result-label">${label}</div>
          <div class="result-progress">
            <div class="result-fill" style="width: ${percentage}%"></div>
          </div>
          <div class="result-count">${count} vote${count !== 1 ? 's' : ''}</div>
        </div>
      `;
    });
    
    container.innerHTML = html;
  }
});
</script>