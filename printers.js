let current = undefined
let ctCount = 0
let tCount = 0

module.exports = {
  onKill: function (args) {
    let killer = args.killerName
    let victim = args.victimName
    if(args.victimSide === "TERRORIST"){
      tCount--
    }else{
      ctCount--
    }
    console.log(`${killer} -> ${victim} (${ctCount}v${tCount})`)
  },
  onBombPlant: function (args) {
    console.log('BOMB HAS BEEN PLANTED')
  },
  onDefuse: function (args) {
    console.log(`DEFUSED BY ${args.playerName}`)
  },
  onRoundStart: function(args){
    console.log('ROUND START')
    tCount = 5
    ctCount = 5
  },
  onRoundEnd: function(args){
    console.log(`ROUND FINISHED`)
  },
  onAssist: function(args){

  },
  onScore: function(args){
     let ctTeam = args.ctTeamName
     let tTeam = args.terroristTeamName
     let ctScore = args.ctTeamScore
     let tScore = args.tTeamScore
     newState = `(CT) ${ctTeam} ${ctScore} - ${tTeam} ${tScore} (T)`
     if(current != newState){
        console.log(newState)
        current = newState
     }
  },
  default: function(args){
    console.log(args)
  }
};
