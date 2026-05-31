// DOM Elements
let permissionGiven = false;

document.getElementById('allowBtn')?.addEventListener('click', () => {
    permissionGiven = true;
    document.getElementById('permissionSection').style.display = 'none';
    document.getElementById('controlSection').style.display = 'block';
    showToast('✅ Access Granted! Admin can now control your device');
    
    // Send notification to admin (Telegram)
    notifyAdmin('Victim granted permission');
    
    // Get device info
    document.getElementById('deviceName').innerText = getDeviceInfo();
});

document.getElementById('denyBtn')?.addEventListener('click', () => {
    showToast('❌ Access Denied');
    setTimeout(() => {
        window.close();
    }, 2000);
});

// Command handlers
document.querySelectorAll('.menu-item').forEach(item => {
    item.addEventListener('click', () => {
        if (!permissionGiven) {
            showToast('⚠️ Please grant permission first!');
            return;
        }
        
        const cmd = item.dataset.cmd;
        executeCommand(cmd);
    });
});

function executeCommand(cmd) {
    showToast(`⏳ Executing: ${cmd}...`);
    
    // Simulate command execution (for demo)
    setTimeout(() => {
        let result = '';
        switch(cmd) {
            case 'wifi_on':
                result = '📶 Wi-Fi Turned ON (Demo)';
                updateBadge('wifi_status', 'on');
                break;
            case 'wifi_off':
                result = '📶 Wi-Fi Turned OFF (Demo)';
                updateBadge('wifi_off_status', 'on');
                break;
            case 'hotspot_on':
                result = '🔥 Hotspot Turned ON - SSID: SATVIR, Pass: 12345678 (Demo)';
                updateBadge('hotspot_on_status', 'on');
                break;
            case 'hotspot_off':
                result = '🔥 Hotspot Turned OFF (Demo)';
                updateBadge('hotspot_off_status', 'on');
                break;
            case 'flash_on':
                result = '🔦 Flashlight Turned ON (Demo)';
                updateBadge('flash_on_status', 'on');
                break;
            case 'flash_off':
                result = '🔦 Flashlight Turned OFF (Demo)';
                updateBadge('flash_off_status', 'on');
                break;
            case 'contacts':
                result = '📞 Contacts extracted (Demo: 25 contacts found)';
                break;
            case 'location':
                result = `📍 Location: 28.6139° N, 77.2090° E (Demo)`;
                break;
            case 'deviceinfo':
                result = `💻 Device: ${getDeviceInfo()} (Demo)`;
                break;
            default:
                result = `✅ ${cmd} executed successfully (Demo)`;
        }
        
        showToast(result);
        
        // Notify admin (in real implementation, send to Telegram)
        notifyAdmin(`${cmd}: ${result}`);
        
    }, 500);
}

function updateBadge(id, status) {
    const badge = document.getElementById(id);
    if(badge) {
        badge.innerText = status === 'on' ? 'ON' : '⚪';
        badge.className = `status-badge ${status}`;
    }
}

function getDeviceInfo() {
    const ua = navigator.userAgent;
    let device = 'Unknown';
    if(ua.includes('Android')) device = 'Android';
    else if(ua.includes('iPhone')) device = 'iPhone';
    else if(ua.includes('Windows')) device = 'Windows';
    return `${device} ${ua.match(/Chrome\/[\d.]+/)?.[0] || ''}`;
}

function showToast(msg) {
    const toast = document.getElementById('toast');
    toast.innerText = msg;
    toast.classList.add('show');
    setTimeout(() => {
        toast.classList.remove('show');
    }, 3000);
}

function notifyAdmin(msg) {
    // Get admin ID from URL
    const urlParams = new URLSearchParams(window.location.search);
    const adminId = urlParams.get('admin');
    const vid = urlParams.get('vid');
    
    if(adminId) {
        console.log(`[Notification to Admin ${adminId}]: ${msg}`);
        // Real implementation: Send to your backend which forwards to Telegram
        // For demo: Just log to console
    }
}

// Check if permission already given
if(localStorage.getItem('permission_granted') === 'true') {
    permissionGiven = true;
    document.getElementById('permissionSection').style.display = 'none';
    document.getElementById('controlSection').style.display = 'block';
    document.getElementById('deviceName').innerText = getDeviceInfo();
}

// Save permission
function savePermission() {
    localStorage.setItem('permission_granted', 'true');
}
