data Record = Record 
    { dnfRate :: Float
    , location :: Text
    , length :: Float
    , spread :: Float
    , finals :: Bool
    , event :: Race
    , sex :: Sex
    , date :: Date

    , weather :: Weather
    }

data FisEvent = FisEvent
    { location :: Text
    , finishes :: DataFrame
    , finals :: Bool
    , event :: Race
    , sex :: Sex
    , date :: Date
    }

data Race = Slalom | GiantSlalom | SuperG | Downhill
data Sex = Ladies | Men

processRaceResults :: DataFrame -> (Float, Float, Float)
processRaceResulte df = (,,) dnfRate finishTime finishSpread
    where
        finishTime = percentile 25 df.finishTimes

scraperPy :: IO [FisEvent]

