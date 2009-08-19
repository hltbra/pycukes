spec_number=1
should_be_equal(){
    if [ "$1" != "$2" ]; then
        echo "$spec_number - FAILED!"
    else
        echo "$spec_number - OK"
    fi
}

should_be_equal "`pycukes specs/bowling_game.story`"  "`cat bowling_game_output`"
should_be_equal "`pycukes specs/bowling_game.story specs/calculator.story`" "`cat bowling_and_calculator_output`"
should_be_equal "`pycukes`" "`cat bowling_and_calculator_output`"
