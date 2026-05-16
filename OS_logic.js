const apps = {
    store: {
        title: "Z-Store",
        content: `
            <div class="app-page">
                <h3>Featured Apps</h3>
                <div class="store-item">Cube Spy <button>Install</button></div>
                <div class="store-item">Zsports <button>Install</button></div>
                <hr>
                <p>Connected to ZTL Repositories</p>
            </div>`
    },
    files: {
        title: "Z-Files",
        content: `
            <div class="app-page">
                <ul id="file-list">
                    <li>Documents/</li>
                    <li>Projects/</li>
                    <li>system_root.zew</li>
                </ul>
            </div>`
    },
    camera: {
        title: "Camera",
        content: `
            <div class="app-page camera-view">
                <div class="viewfinder"></div>
                <button onclick="alert('Shutter Pressed')">CAPTURE</button>
            </div>`
    },
    settings: {
        title: "Settings",
        content: `
            <div class="app-page">
                <label>System: ZewpolOS 3.5 Grass Field</label><br>
                <label>Kernel: Linux 6.x (Modified)</label><br>
                <button onclick="location.reload()">Reboot UI</button>
            </div>`
    }
};

function openApp(appKey) {
    const app = apps[appKey];
    document.getElementById('app-title').innerText = app.title;
    document.getElementById('app-content').innerHTML = app.content;
    document.getElementById('app-layer').classList.remove('hidden');
}

function closeApp() {
    document.getElementById('app-layer').classList.add('hidden');
}

// Simple clock update
setInterval(() => {
    document.getElementById('clock').innerText = new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'});
}, 1000);
async function loadFiles() {
    const res = await fetch('/api/files/browse'); // Python endpoint using os.listdir()
    const data = await res.json();
    const list = document.getElementById('file-list');
    list.innerHTML = data.files.map(f => `<li>${f}</li>`).join('');
}
async function startCamera() {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    const video = document.createElement('video');
    video.srcObject = stream;
    video.play();
    document.getElementById('app-content').appendChild(video);
}


