alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

getIndex(){ #arr, val
    my_array=$1
    value=$2

    for i in "${!my_array[@]}"; do
    if [[ "${my_array[$i]}" = "${value}" ]]; then
        echo "${i}";
    fi
    done
}

decrypt(){ #message, key

    message=$1
    key=$2

    result=""

    for l in "${$message^^}"; do
        if containsElement "${$l^^}" "${alpha[@]}"; then #if the letter is actually a letter
            #find the corresponding ciphertext letter in the alphabet
            result="$result$(alpha[($(getIndex $alpha $l) - $key) % ${#alpha[@]}])"
        else
            result=$result $l
        fi
    done

    echo $result
}

# break ceaser 
break_caesar(){ #message, type, l, WORDS

    message=$1
    type=$2
    l=$3
    WORDS=$4
    
    echo -e "Decrypting: "$message"\n ------ \n"
    
    shift=-1
    [[ $type =  "%" ]] && realWords=0 || realWords=()
    total=l # 0.8 -> % | 100 -> specified
    
    while ( [ "$type" == "%" ] && (( (${#message[@]} - ${#realWords[@]}) > (${#message[@]} * total) )) ) || ( [ "$type" == "x" ] && (( shift <= l )) ); do

        shift+=1

        if [ $type = "x" ]; then
            realWords+=(0)
        fi
        
        n_message=$(decrypt $message $shift)
        
        echo $n_message

        n_words=( $n_message )
        
        for i in $n_words; do
            for l in $i; do
                if ! containsElement "${$l^^}" "${alpha[@]}"; then
                    i=${i//$l/}
                fi
            done

            if containsElement "${$i,,}" "${WORDS[@]}"; then
                if [[ $type = "x" ]]; then
                    realWords[c]+=1
                else
                    realWords+=1
                fi
            fi
        done
    done

    [[ $type = "x" ]] && r_val=$(getIndex max(realWords) $realWords) || r_val=$shift

    echo  $r_val # the most likely shift value as an integer |
}

# main

main(){

    wordlist=$(cat $4)

    vals=$(break_caesar $1 $2 $3 $wordlist) # 1-text (input text) \ 2-type (%, x) \ 3-l (condition: 100 words, 0.8 %) \ 4-WORDS (language wordlist)

    key="${vals[0]}"
    text="${vals[1]}"
}

# Args to add: | keys to ignore
# ARGs: | input-text | first-match percentage (%) / best-match tries (x) | condition (100 words, 0.8 %)  | language wordlist
main "$1" "$2" "$3" "$4"