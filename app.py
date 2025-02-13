<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Information</title>
    <style>
/* General body styling */
/* General body styling */
body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #6a11cb, #2575fc);
    color: #fff;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    overflow: hidden;
}

/* Container styling */
.container {
    background: rgba(255, 255, 255, 0.9); /* Slight transparency */
    backdrop-filter: blur(5px);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3);
    text-align: center;
    animation: fadeIn 1.5s ease-out;
    width: 90%; /* Adjusts to smaller screens */
    max-width: 400px;
    background-image: url('static/naruto.png'); /* Naruto image as background */
    background-size: cover;
    background-position: center;
}

/* Heading styling */
h1 {
    font-size: 2rem;
    margin-bottom: 10px;
    color: #ffcccb;
    animation: slideDown 1s ease-out;
}

/* Paragraph styling */
p {
    font-size: 1rem; /* Reduced font size for smaller screens */
    margin: 10px 0;
    color: #333;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
}

/* Anchor styling */
a {
    color: #ffcccb;
    text-decoration: none;
    font-weight: bold;
    transition: color 0.3s ease-in-out;
}

a:hover {
    color: #ffeb3b;
}

/* QR code container styling */
.qr-code {
    margin-top: 20px;
    padding: 10px;
    background: #fff;
    border-radius: 10px;
    display: inline-block;
    animation: zoomIn 1s ease-in-out;
}

/* Keyframe animations */
@keyframes fadeIn {
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
}

@keyframes slideDown {
    0% {
        transform: translateY(-30px);
        opacity: 0;
    }
    100% {
        transform: translateY(0);
        opacity: 1;
    }
}

@keyframes zoomIn {
    0% {
        transform: scale(0.5);
        opacity: 0;
    }
    100% {
        transform: scale(1);
        opacity: 1;
    }
}

/* Responsive design for smaller screens */
@media (max-width: 768px) {
    .container {
        width: 95%;
        padding: 15px;
        background-size: contain; /* Adjusts image scaling */
    }

    h1 {
        font-size: 1.5rem; /* Smaller heading */
    }

    p {
        font-size: 0.9rem; /* Smaller paragraph text */
    }

    .qr-code {
        margin-top: 15px;
        padding: 8px;
    }
}

@media (max-width: 480px) {
    .container {
        width: 100%; /* Full width for very small screens */
        padding: 10px;
    }

    h1 {
        font-size: 1.2rem; /* Further reduce heading size */
    }

    p {
        font-size: 0.8rem; /* Further reduce paragraph text */
    }

    .qr-code {
        margin-top: 10px;
        padding: 6px;
    }
}

    </style>
</head>
<body>
    <div class="container">
        <h1>Nikhil Patil</h1>
        <p><strong>Phone:</strong> +91 7975053002</p>
        <p><strong>instagram:</strong> <a href="https://www.instagram.com/_nikhil__patil96k?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==" target="_blank">@nikhil_patil</a></p>
        <div class="qr-code">
        </div>
    </div>
</body>
</html>
