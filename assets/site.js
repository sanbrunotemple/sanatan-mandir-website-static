
document.querySelectorAll('[data-dismiss]').forEach(b=>b.onclick=()=>b.parentElement.remove());
const q=document.querySelector('#eventSearch'); if(q){q.addEventListener('input',()=>{const v=q.value.toLowerCase();document.querySelectorAll('.event-row').forEach(r=>r.style.display=r.textContent.toLowerCase().includes(v)?'':'none');document.querySelectorAll('.month').forEach(m=>{const any=[...m.querySelectorAll('.event-row')].some(r=>r.style.display!=='none');m.style.display=any?'':'none'})})}
