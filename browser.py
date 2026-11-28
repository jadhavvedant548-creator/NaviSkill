from playwright.sync_api import sync_playwright
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']); page=b.new_page(viewport={'width':1280,'height':900});page.set_default_timeout(2500); errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 # In-memory storage for set_content on about:blank (actual origin navigation blocked).
 html=(root/'NaviSkill_Offline.html').read_text().replace('<head>','<head><script>const __testStore=new Map();Object.defineProperty(window,"localStorage",{value:{getItem:k=>__testStore.get(k)??null,setItem:(k,v)=>__testStore.set(k,String(v)),removeItem:k=>__testStore.delete(k)}})</script>',1)
 page.set_content(html,wait_until='load'); assert page.locator('nav a').count()==7
 for lang in ['mr','hi','en']:
  page.select_option('#language',lang);assert page.locator('html').get_attribute('lang')==lang;assert page.locator('[data-t=edition]').inner_text()=='NaviSkill'
 print('Browser: render, seven tabs and three language switches PASS')
 page.click('#v13ai');page.fill('#v13input','train ticket');page.click('#v13offline');assert 'station' in page.locator('#v13out').inner_text().lower();page.click('#v13online');assert 'consent' in page.locator('#v13out').inner_text().lower() or 'internet' in page.locator('#v13out').inner_text().lower();page.click('#v13close');page.click('#v13shield');page.click('#v13sample');page.click('#v13offline');assert 'credential' in page.locator('#v13out').inner_text().lower();page.click('#v13close');print('Browser: offline AI, online prerequisite fallback, scam sample PASS')
 page.click('#c14-add');assert page.locator('#c14-person').input_value().startswith('NS-');page.click('#c14-before');
 for i in range(10):page.locator('#c14-assess button').first.click()
 page.locator('#c14-skills input').first.check();page.click('#c14-session');page.click('#c14-after');
 for i in range(10):page.locator('#c14-assess button').nth(1).click()
 page.select_option('#c14-rating','4');page.select_option('#c14-difficulty','language');page.click('#c14-feedback');assert '1' in page.locator('#c14-metrics').inner_text();page.select_option('#c14-passperson',page.locator('#c14-person').input_value());assert 'NS-' in page.locator('#c14-report').inner_text();page.on('dialog',lambda d:d.accept());page.click('#c14-delete');assert page.locator('#c14-person option').count()==1;print('Browser: learner, both assessments, session, feedback, passport, deletion PASS')
 assert page.locator('[data-city]').count()==6
 for id in ['upi','train','gov','sheet','bill','appointment']:
  page.locator(f'[data-city="{id}"]').click();assert page.locator('#guide-start').is_visible();page.keyboard.press('Escape')
 print('Browser: six city destinations open PASS')
 page.click('#quiz-feature-start');
 for i in range(10):
  page.locator('#content [data-n]').first.click();page.click('#next')
 assert page.locator('#content').inner_text().strip();page.keyboard.press('Escape');print('Browser: ten-question quiz completion PASS')
 page.set_viewport_size({'width':390,'height':844});print('Mobile document width:',page.evaluate('document.documentElement.scrollWidth'));assert not errors,errors;print('Browser: no uncaught errors in exercised flows PASS');b.close()
