#!/data/data/com.termux/files/usr/bin/bash
# ╦  ╦┌─┐┬ ┬┌┬┐┌─┐┌─┐┬─┐┬─┐  ╔═╗┌┐┌┌─┐┌─┐┬─┐  ╔═╗┌─┐┌─┐┬  ┌─┐┬─┐┌┐┌┬┌─┐
# ╚╗╔╝├┤ │ │ │ │  ├┤ ├┤ ├┬┘├┬┘  ║  │││├┤ ├┤ ├┬┘  ╠═╣├┤ ├┤ │  ├┤ ├┬┘││││├┤ 
#  ╚╝ └─┘└─┘ ┴ └─┘└─┘┴└─┴└─  ╚═╝┘└┘└─┘└─┘┴└─  ╩ ╩└─┘└─┘┴─┘└─┘┴└─ ┘└┘┴└─┘
#                            HENRY v3.1 | E2EE MASS BLASTER | CUSTOM DELAY
# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║ HENRY E2EE MASS TOOL | ${BOLD}CUSTOM DELAY CONTROL${NC} | TERMUX | EAAD6V7 TOKENS  ║
# ╚══════════════════════════════════════════════════════════════════════════════╝

clear
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m'
BOLD='\033[1m'

banner() {
    clear
    echo -e "${CYAN}
╔══════════════════════════════════════════════════════════════════════════════╗
║  ██████╗██╗  ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗  ██████╗  ║
║  ██╔══██╗██║  ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗██╔═══╝  ║
║  ██████╔╝███████║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝██║      ║
║  ██╔══██╗██╔══██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗██║      ║
║  ██║  ██║██║  ██║███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║╚██████╗  ║
║  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                       ${BOLD}HENRY v3.1 - CUSTOM SPEED CONTROL${NC}                     ║
║  CREATED BY: HENRY | CYBER GHOST 2077 | ${RED}0.5s-60s DELAY${NC} | 2026          ║
║  💎 ${GREEN}EAAD6V7 TOKENS${NC} | ${PURPLE}SPEED: SLOW/NORMAL/FAST/TURBO${NC} | TERMUX 💎    ║
╚══════════════════════════════════════════════════════════════════════════════╝
    ${NC}"
}

loading() {
    echo -ne "${YELLOW}🔥 HENRY SPEED PROTOCOLS LOADING"
    for i in {1..6}; do
        echo -ne "."
        sleep 0.2
    done
    echo -e "\n${GREEN}✅ HENRY SPEED SELECTOR READY${NC}\n"
}

speed_selector() {
    echo -e "${BLUE}⚡ HENRY SPEED MODE SELECTOR:${NC}"
    echo "1) ${GREEN}SLOW${NC}     - 15-30s  (MAX SAFE)"
    echo "2) ${GREEN}NORMAL${NC}  - 8-15s   (RECOMMENDED)"
    echo "3) ${GREEN}FAST${NC}   - 3-8s    (HIGH SPEED)"
    echo "4) ${GREEN}TURBO${NC}  - 0.5-3s  (RISKY 🔥)"
    echo "5) ${GREEN}CUSTOM${NC} - Enter seconds"
    
    read -p "🎯 CHOOSE SPEED (1-5): " choice
    
    case $choice in
        1) MIN_DELAY=15; MAX_DELAY=30; SPEED="SLOW (15-30s)" ;;
        2) MIN_DELAY=8; MAX_DELAY=15; SPEED="NORMAL (8-15s)" ;;
        3) MIN_DELAY=3; MAX_DELAY=8; SPEED="FAST (3-8s)" ;;
        4) MIN_DELAY=1; MAX_DELAY=3; SPEED="TURBO (0.5-3s)" ;;
        5) 
            read -p "⏱️ Enter MIN delay (seconds): " MIN_DELAY
            read -p "⏱️ Enter MAX delay (seconds): " MAX_DELAY
            SPEED="CUSTOM ($MIN_DELAY-$MAX_DELAY s)"
            ;;
        *) echo -e "${RED}❌ Invalid! Using NORMAL${NC}"; MIN_DELAY=8; MAX_DELAY=15; SPEED="NORMAL";;
    esac
    
    echo -e "\n${GREEN}✅ SPEED SET: $SPEED${NC}"
}

get_token() {
    echo -e "\n${BLUE}👑 ENTER YOUR EAAD6V7 TOKEN:${NC}"
    read -p "👉 TOKEN: " TOKEN
    if [[ ! "$TOKEN" =~ ^EAAD ]]; then
        echo -e "${RED}❌ INVALID! Must start with EAAD${NC}"
        exit 1
    fi
}

get_targets() {
    echo -e "\n${BLUE}📱 TARGET USER IDs (one per line, Ctrl+D):${NC}"
    cat > /data/data/com.termux/files/home/henry_targets.txt
    TARGETS=$(cat /data/data/com.termux/files/home/henry_targets.txt)
    rm -f /data/data/com.termux/files/home/henry_targets.txt
    TARGET_COUNT=$(echo "$TARGETS" | wc -l)
}

get_messages() {
    echo -e "\n${BLUE}💬 MESSAGES (one per line, Ctrl+D):${NC}"
    cat > /data/data/com.termux/files/home/henry_messages.txt
    MESSAGES=$(cat /data/data/com.termux/files/home/henry_messages.txt)
    rm -f /data/data/com.termux/files/home/henry_messages.txt
    MSG_COUNT=$(echo "$MESSAGES" | wc -l)
}

stats() {
    local sent=$1 total=$2
    percent=$((sent * 100 / total))
    bar=$(printf "█%.0s" $(seq 1 $((percent/2))))
    spaces=$(printf " %.0s" $(seq 1 $((50-percent/2))))
    echo -ne "${CYAN}\r📊 $sent/$total ($percent%) |$bar$spaces| SPEED: ${YELLOW}$SPEED${NC} | ${GREEN}$sent SENT${NC}"
}

send_message() {
    local target=$1
    local msg=$(echo "$MESSAGES" | shuf -n 1)
    
    response=$(curl -s -w "%{http_code}" -X POST "https://graph.facebook.com/v18.0/me/messages" \
        -H "Authorization: Bearer $TOKEN" \
        -H "Content-Type: application/json" \
        -d "{\"recipient\":{\"id\":\"$target\"},\"message\":{\"text\":\"$msg\"}}" \
        -o /dev/null --max-time 10)
    
    if [[ "$response" == "200" ]]; then
        echo -ne "${GREEN}✅ "
    else
        echo -ne "${RED}❌ "
    fi
    
    echo "$(date '+%H:%M:%S') | $target | $msg | HTTP:$response" >> "henry_log_$(date +%Y%m%d_%H%M%S).txt"
}

mass_blast() {
    local counter=0
    echo -e "\n${PURPLE}🚀 HENRY $SPEED BLAST INITIATED${NC}"
    echo "📅 $(date)"
    echo "🎯 Targets: $TARGET_COUNT"
    echo "💬 Messages: $MSG_COUNT"
    echo "⚡ Delay: ${MIN_DELAY}-${MAX_DELAY}s"
    echo "─────────────────────────────"
    echo ""
    
    while true; do
        for target in $TARGETS; do
            send_message "$target"
            ((counter++))
            stats $counter $((TARGET_COUNT * 1000))  # Infinite loop
            
            # HENRY CUSTOM DELAY
            DELAY=$((MIN_DELAY + RANDOM % (MAX_DELAY - MIN_DELAY + 1)))
            sleep $DELAY
        done
        echo ""
        echo -e "${YELLOW}🔄 Full cycle complete ($counter total). Restarting...${NC}"
        sleep 3
    done
}

main_menu() {
    banner
    loading
    speed_selector  # 🔥 NEW SPEED SELECTOR!
    
    get_token
    get_targets
    get_messages
    
    banner
    echo -e "${GREEN}🎉 HENRY $SPEED MODE READY!${NC}"
    echo -e "${YELLOW}⚠️  Logs: henry_log_*.txt | Ctrl+C to stop${NC}"
    echo ""
    read -p "🚀 START $SPEED BLAST? (y/N): " confirm
    
    if [[ $confirm =~ ^[Yy]$ ]]; then
        mass_blast
    else
        echo -e "${RED}❌ HENRY CANCELLED${NC}"
    fi
}

# HENRY v3.1 LAUNCH
main_menu
