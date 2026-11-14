# Metadata for all videos

Each entry: title, description, thumbnail prompt for ChatGPT (image generation, 1080x1920). ChatGPT sometimes misspells text in images. If it does, regenerate or fix the text in an image editor.

---

## 1. ux-5-states: The 5 UX states every app needs

**Title:** Your App Looks Broken Without These 5 States

**Description:**
Your app shows a blank screen, and users think it's broken, even when the code works. Every screen needs five states: loading, empty, error, offline and not found. Here's how to show each one in plain words.

#react #webdev #uxdesign #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text across the top: "BLANK SCREEN = BUG?" with "BUG?" in yellow. Centre: a flat, minimal illustration of a phone showing an empty white screen with one small grey placeholder card. Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 2. ux-details: 5 small UX details that make an app feel professional

**Title:** 5 Small UX Details That Make Your App Feel Professional

**Description:**
Two apps can do the same job, but one feels cheap and the other feels professional. The difference is small details: field-level errors, a delete confirmation, clear feedback, helper text and accessibility. Each one takes minutes to add.

#react #webdev #uxdesign #accessibility #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Top: small blue label "5 DETAILS" and five short segments in a row, the first two filled. Centre: a minimal dark UI card with a delete confirmation dialog, the "Cancel" button outlined in blue and a red "Delete" button. Large bold white text below: "SMALL DETAILS." and "BIG DIFFERENCE." Flat design, crisp edges, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 3. cors-failed-to-fetch: "Failed to fetch" in React? It's probably CORS

**Title:** "Failed to fetch" in React? It's Probably CORS

**Description:**
Your login fails with "Failed to fetch," but your code looks fine. The real reason is in the browser console: CORS. Your app and your API run on different addresses, and the API has to allow your app's address. Here's how to find it and fix it.

#react #cors #webdev #debugging #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "FAILED TO FETCH?" with "FETCH?" in red. Centre: a flat illustration of a browser window in the middle, a red blocked-arrow between two small boxes labelled "APP" and "API", and a dark console panel below with one red line of text. Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 4. react-typing-lag: Why your React app gets slow when you type

**Title:** Why Your React App Gets Slow When You Type

**Description:**
Every keystroke re-renders the whole page, including every note card. With ten notes, each letter can cost about 200 milliseconds. Here's the fix: move the form's state into its own component, memoize the cards, and keep the handlers stable. And why memo doesn't fix everything.

#react #reactjs #webdev #performance #frontend #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "LAGGY TYPING?" with "LAGGY" in red. Centre: a flat illustration of a text input with a cursor, and below it a grid of ten small grey cards, with a red bar at the bottom reading "200 ms per letter". Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 5. dark-mode-react: Dark mode in React in 5 minutes (done right)

**Title:** Dark Mode in React: Stop Hard-Coding Colors

**Description:**
Most broken dark modes only change the background, so the text becomes unreadable. The fix: every color comes from one place, as a CSS variable. Define the dark values once, add a toggle that remembers the choice, and use the system setting as the default.

#react #darkmode #css #webdev #frontend #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "DARK MODE BROKEN?" with "BROKEN?" in red. Centre: two flat mini app cards side by side, the left one black with almost invisible grey text, the right one dark with bright readable text, and a toggle switch below the right card in blue. Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 6. idor-notes-app: Your API might leak other users' data (IDOR)

**Title:** Your API Might Leak Other Users' Data (IDOR)

**Description:**
Logging in proves who you are. The server still has to check that the item belongs to you. Without that check, anyone can change a number in the URL and read or delete someone else's note. This is called an IDOR. Here's how to stop it, and why the server should return 404, not 403.

#security #api #webdev #backend #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "ANYONE CAN READ IT" with "READ" in red. Centre: a flat browser address bar showing a URL ending in a highlighted number, with a small red lock icon and a flat note card beneath it marked "PRIVATE". Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 7. cache-invalidation: Why your API returns old data

**Title:** Why Your API Returns Old Data (Cache Invalidation)

**Description:**
You create a note, but the list doesn't show it. The API is answering from a cache that's out of date. Here's how to spot it with the X-Cache header, and how a version number in the cache key fixes it for just one user.

#backend #caching #api #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "STILL MISSING?" with "MISSING?" in yellow. Centre: a flat list of three note rows with a fourth faint row marked with a dashed outline, beside a small badge reading "X-Cache: HIT" in red. Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 8. clean-architecture-aspnet: Clean architecture in ASP.NET Core

**Title:** Clean Architecture in ASP.NET Core: One Rule, One Place

**Description:**
Your controller checks for 5 characters while your service checks for 3, and now the rule drifts apart. Here's a clean split: the controller handles HTTP, the service holds the rules, and the repository stores data. Every write goes through the service, and switching databases changes one line.

#aspnet #dotnet #csharp #architecture #webdev #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "ONE RULE. ONE PLACE." with "ONE PLACE." in blue. Centre: three flat stacked boxes labelled "CONTROLLER", "SERVICE" and "REPOSITORY", with arrows between them and a dashed red bypass arrow that is crossed out. Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 9. api-pagination: Pagination in a Notes API

**Title:** Pagination in APIs: Stop Sending Every Row

**Description:**
Your notes API sends every note in one response. It works with ten notes, then the app freezes at ten thousand. Pagination sends one page at a time, with a cap on the page size and a check on the numbers. Code: https://github.com/Vishal-270504/notes-app

#api #backend #typescript #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "TOO MUCH DATA?" with "DATA?" in yellow. Centre: a flat tall stack of thin grey rows that runs off the top of the frame, with a clean block of three rows highlighted in blue beneath it labelled "PAGE 1". Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 10. api-validation: Validation in a Notes API

**Title:** API Validation: Stop Garbage at the Door

**Description:**
Someone sends a note with no title, and your API saves it anyway. Validation checks every request before it reaches the database, and rejects bad data with a clear 400 Bad Request. Code: https://github.com/Vishal-270504/notes-app

#api #backend #validation #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "GARBAGE IN?" with "IN?" in red. Centre: a flat door-shaped checkpoint in blue, with a red rejected box on one side and three clean green rows on the other, labelled "400". Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 11. api-rate-limiting: Rate limiting in an API

**Title:** Rate Limiting: Stop One Client Taking Down Your API

**Description:**
One script can send a thousand requests a second, and your server slows down for everyone. Rate limiting gives each client a fixed number of requests per minute. Extra requests get a 429 Too Many Requests, so the rest of your users keep working. Code: https://github.com/Vishal-270504/notes-app

#api #backend #ratelimiting #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "429" in red with "TOO MANY" in white below it. Centre: a flat counter bar almost full in blue labelled "60 / minute", with a single red dot flying past it. Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.

---

## 12. api-error-handling: Error handling in an API

**Title:** API Error Handling: One Place, One Response

**Description:**
When something breaks, your API shouldn't show a wall of stack trace to the user. One central error handler turns every failure into one response shape: a clear status code and a short message. The full details stay in the server logs. Code: https://github.com/Vishal-270504/notes-app

#api #backend #errorhandling #webdev #coding #shorts

**Thumbnail prompt for ChatGPT:**
> Vertical 9:16 image, 1080x1920. Near-black background. Large bold white text at the top: "SHOWING STACK TRACES?" with "STACK TRACES?" in red. Centre: a flat dark panel with three faint red error lines on the left, a single blue funnel in the middle, and one clean white card on the right labelled "404 Not found". Clean, high contrast, lots of negative space. No people, no logos, no real brand names, no emojis.
