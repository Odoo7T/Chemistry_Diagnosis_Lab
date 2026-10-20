# -*- coding: utf-8 -*-
"""
run_global.py
=============
تشغيل نظام خبير الكيمياء برابط عالمي (Cloudflare Tunnel)
المصدر: لابتوبك بالكامل.
إذا أغلقت النافذة أو ضغطت Ctrl+C، يقفل التطبيق عند الجميع فوراً!
"""

import subprocess
import sys
import time
import threading
import socket
import re
import os

# ضبط ترميز النصوص في ويندوز
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    if hasattr(sys.stderr, 'reconfigure'):
        sys.stderr.reconfigure(encoding='utf-8')
except Exception:
    pass

PORT = 5000
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLOUDFLARED_PATH = os.path.join(BASE_DIR, "cloudflared.exe")


def get_local_ip():
    """الحصول على الآي بي المحلي داخل شبكة الواي فاي."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def copy_to_clipboard(text):
    """نسخ الرابط تلقائياً إلى الحافظة."""
    try:
        subprocess.run("clip", input=text.strip(), text=True, check=True)
        return True
    except Exception:
        return False


def start_waitress_server():
    """تشغيل خادم الويب في الخلفية."""
    try:
        from waitress import serve
        from app import app
        serve(app, host="0.0.0.0", port=PORT, _quiet=True)
    except Exception as e:
        print(f"\n[!] خطأ في تشغيل السيرفر: {e}", flush=True)


def main():
    print("=" * 60, flush=True)
    print("   🚀 تشغيل نظام خبير الكيمياء برابط جلوبال (Global Server)   ", flush=True)
    print("=" * 60, flush=True)

    # 1. تشغيل خادم بايثون
    print("[1/2] ⏳ جاري تشغيل السيرفر على لابتوبك...", flush=True)
    server_thread = threading.Thread(target=start_waitress_server, daemon=True)
    server_thread.start()
    time.sleep(1.5)

    local_ip = get_local_ip()
    print(f"      ✓ السيرفر الداخلي يعمل بنجاح على المنفذ {PORT}", flush=True)

    # 2. تشغيل نفق Cloudflare المباشر والسريع
    print("[2/2] 🌐 جاري إنشاء رابط جلوبال مستقر وسريع...", flush=True)

    cf_cmd = [
        CLOUDFLARED_PATH,
        "tunnel",
        "--url", f"http://127.0.0.1:{PORT}"
    ]

    try:
        proc = subprocess.Popen(
            cf_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            stdin=subprocess.DEVNULL,
            text=True,
            encoding="utf-8",
            errors="replace"
        )
    except Exception as e:
        print(f"[!] خطأ في تشغيل النفق: {e}", flush=True)
        return

    public_url = None
    url_pattern = re.compile(r'https://[a-zA-Z0-9\-]+\.trycloudflare\.com')

    # قراءة الرابط من مخرجات السيرفر
    start_wait = time.time()
    for line in iter(proc.stdout.readline, ''):
        match = url_pattern.search(line)
        if match:
            public_url = match.group(0)
            break
        if time.time() - start_wait > 25:
            break

    # تفريغ المخرجات في الخلفية لضمان عدم امتلاء الـ Buffer
    def drain_output(stream):
        try:
            for _ in iter(stream.readline, ''):
                pass
        except Exception:
            pass

    threading.Thread(target=drain_output, args=(proc.stdout,), daemon=True).start()

    if public_url:
        copied = copy_to_clipboard(public_url)
        print("\n" + "═" * 60, flush=True)
        print("  🎉 تم تشغيل التطبيق بنجاح والرابط شغال وثابت تماماً!", flush=True)
        print("═" * 60, flush=True)
        print(f"\n  🌐 الرابط العام (ابعت ده لصحابك في أي مكان):", flush=True)
        print(f"  👉  {public_url}  👈\n", flush=True)
        if copied:
            print("  📋 (تم نسخ الرابط في الـ Clipboard تلقائياً - دوس Ctrl+V على طول)", flush=True)
        print("-" * 60, flush=True)
        print(f"  🏠 رابط الدخول لمن معك على نفس شبكة الواي فاي:", flush=True)
        print(f"      http://{local_ip}:{PORT}", flush=True)
        print(f"  💻 رابطك أنت على نفس اللاب:", flush=True)
        print(f"      http://127.0.0.1:{PORT}", flush=True)
        print("═" * 60, flush=True)
        print("  ⚠️  ملاحظة هامة:", flush=True)
        print("      • اللاب بتاعك هو المصدر الأساسي للسيرفر.", flush=True)
        print("      • خلي النافذة دي مفتوحة طول ما أصحابك بيستخدموا الموقع.", flush=True)
        print("      • لو قفلت النافذة دي أو ضغطت Ctrl + C، هيقفل عندهم فوراً.", flush=True)
        print("═" * 60 + "\n", flush=True)

        try:
            proc.wait()
        except KeyboardInterrupt:
            print("\n[!] جاري إيقاف السيرفر والرابط...", flush=True)
            proc.terminate()
            print("[✓] تم إيقاف السيرفر بنجاح. الرابط اتقفل عند الجميع.", flush=True)
    else:
        print("\n[!] لم يتم الحصول على الرابط، تأكد من اتصال الإنترنت وحاول مجدداً.", flush=True)
        proc.terminate()


if __name__ == "__main__":
    main()
