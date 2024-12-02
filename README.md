<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Senior Design Project Showcase Manager</title>
    <style>
        :root {
            --primary-color: #0033A0;
            --secondary-color: #D64309;
            --bg-color: #f5f5f5;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: var(--bg-color);
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 2rem;
        }

        .header {
            background-color: var(--primary-color);
            color: white;
            padding: 2rem 0;
            text-align: center;
            margin-bottom: 2rem;
        }

        .header h1 {
            margin: 0;
            font-size: 2.5rem;
        }

        .github-button {
            display: inline-block;
            padding: 0.8rem 1.5rem;
            background-color: var(--secondary-color);
            color: white;
            text-decoration: none;
            border-radius: 4px;
            margin-top: 1rem;
            transition: background-color 0.3s;
        }

        .github-button:hover {
            background-color: #b53707;
        }

        .section {
            background: white;
            padding: 2rem;
            margin-bottom: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        h2 {
            color: var(--primary-color);
            border-bottom: 2px solid var(--secondary-color);
            padding-bottom: 0.5rem;
        }

        .team-members {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin-top: 1rem;
        }

        .member-card {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 4px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Senior Design Project Showcase Manager</h1>
        <a href="https://github.com/yourusername/your-repo" class="github-button">View on GitHub</a>
    </div>

    <div class="container">
        <div class="section">
            <h2>Project Abstract</h2>
            <p>The Senior Design Showcase, hosted by the College of Engineering each semester, allows students to present their capstone projects. However, faculty overseeing these projects face challenges with the current manual data-entry system, which relies on an inefficient, error-prone online spreadsheet. This process becomes particularly burdensome for faculty managing large numbers of student teams, leading to planning delays and frustration.</p>
            <p>Our project proposes a web application that will streamline data entry and introduce tools to support event planning. By automating many tasks and offering a user-friendly interface, the app will reduce errors, save time, and improve the overall efficiency of organizing the event. This solution will enhance the experience for both faculty and organizers and could serve as a model for other academic departments facing similar challenges.</p>
        </div>

        <div class="section">
            <h2>Project Description</h2>
            <p>We have developed a comprehensive Django-based web application that simplifies the management of senior design showcase projects. Key features include:</p>
            <ul>
                <li>Centralized database for storing project information, student details, and sponsor data</li>
                <li>User-friendly forms for adding and editing project entries</li>
                <li>Role-based access control distinguishing between planners and regular users</li>
                <li>Export functionality for generating CSV reports</li>
                <li>Automated validation to ensure data consistency and completeness</li>
                <li>Support for managing special requirements (power needs, display equipment, etc.)</li>
            </ul>
            
            <h3>Technical Stack</h3>
            <ul>
                <li>Backend: Django framework with SQLite database</li>
                <li>Frontend: HTML/CSS with Angular components</li>
                <li>Authentication: Django's built-in auth system with custom user roles</li>
                <li>Deployment: Configured for hosting on university servers</li>
            </ul>
        </div>

        <div class="section">
            <h2>Team Members</h2>
            <div class="team-members">
                <div class="member-card">
                    <h3>Pierce Rodriguez</h3>
                    <p>Backend Developer</p>
                </div>
                <div class="member-card">
                    <h3>Nolan Stetz</h3>
                    <p>Backend Developer</p>
                </div>
                <div class="member-card">
                    <h3>Abbie Sarmento</h3>
                    <p>Frontend Developer</p>
                </div>
                <div class="member-card">
                    <h3>Ben Brindley</h3>
                    <p>Frontend Developer</p>
                </div>
            </div>
        </div>

        <div class="section">
            <h2>Project Sponsor</h2>
            <p>Donald Plumlee - College of Engineering, Boise State University</p>
        </div>
    </div>
</body>
</html>
