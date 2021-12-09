import { useState, useEffect } from 'react';
import { Container, Grid, Typography, TextField, Button, Link, List, ListItemButton,ListItem, Dialog, DialogTitle, DialogContent} from '@mui/material';
import functions from './functions.js';
function App() {

  const [selectedFunctions, setSelectedFunctions] = useState({});
  const [parentFunction, setParentFunction] = useState({});
  const [userInput, setUserInput] = useState("");
  const [output, setOutput] = useState();
  const [apiData, setApiData] = useState({});
  const [url, setUrl] = useState("http://localhost:5000/");
  const [funcUrl, setFuncUrl] = useState("");
  const [showChildren, setShowChildren] = useState(false);


  


  useEffect(() => {
    fetch('http://localhost:5000/members').then(
      res => res.json()
    )
    .then(
      data => {
        setApiData(data)
        console.log(data)
      }
    )
    .catch(err => console.log(err))
  }, [])


  const handleSubmit = () =>{
    fetch(url+ selectedFunctions.url + '?input=' + userInput).then(
     response => response.json()
   )
   .then(
     data => {
       console.log(data)
       setOutput(data)
     }
   )
  }

  const handleChange = (e, funcName, urlVal, func) =>{

    if (func.hasChildren === false )
    {
      setSelectedFunctions(func);
      setFuncUrl(urlVal);
    }
    if(parentFunction === func) setParentFunction(null);
    else setParentFunction(func);

  }

  const handleChange2 = (e, value) =>{
    setUserInput(e.target.value);
  }

  return (
      <div>
        <style jsx global>{`
      body {
        margin: 0px;
        padding: 0px;
        box-sizing: border-box;
        height: 100vh;
        overflow: hidden;
      }
        `}</style>
        <TopBar />
        <div style={styles.main}>
          <FunctionSelect {...{ selectedFunctions, setSelectedFunctions, handleChange, showChildren, parentFunction}} />
          <Recipe  {...{ setSelectedFunctions, selectedFunctions, handleSubmit, userInput }}/>

          <div style={styles.input}>
            <Input {...{ userInput, setUserInput, handleChange2}}/>
            <Output {...{ userInput, output }} />
          </div>
        </div>
      </div>
  );
}

const TopBar = () => {

  return (
    <div style={styles.topbar}>
      <Grid item>
        <Typography variant='h4'>N0l3Ware </Typography>
      </Grid>
      <Grid >
        <Link href='#' variant='h5' marginRight='1rem' >About/Support</Link>
        <Link href='#' variant='h5' marginRight='1rem'>Options</Link>
      </Grid>
      
    </div>

  );

}

const FunctionSelect = ({ handleChange,showChildren, selectedFunctions,parentFunction, setSelectedFunctions}) =>{

  return (
    <div style={styles.functions}>
      <Typography variant='h6' sx={{border: '1px solid black', padding: '8px'}}>Operations</Typography>
      <List sx={{overflowY: 'scroll', maxHeight: '100%'}}>
        
        {functions.map(func => 
        <>

            <ListItemButton onClick={(e) => handleChange(e, func.name, func.url,func)}>
              <Typography color='blue'>{func.name}</Typography>
            </ListItemButton>
            {func.hasChildren && parentFunction === func &&   func.children.map(child => 
              <List>
                <ListItemButton onClick={(e) => {setSelectedFunctions(child !== selectedFunctions ? child : null)}}>
                  <Typography color='blue'>{child.name}</Typography>
                </ListItemButton>
              </List>
            
            )}

        </>
        )}
        
        
      </List>

      {/*<Dialog open={showChildren === true} onClose={() => setShowChildren(false)}>
        <DialogTitle>Select the function you'd like to perform:</DialogTitle>
        <DialogContent>
          <List>
            {functions.filter(func => func.name === selectedFunctions).then(children.map(child =>
              <ListItemButton onClick={(e) => handleChange(e, child.name, child.url,child)}>
                <Typography color='blue'>{child.name}</Typography>
              </ListItemButton>
            ))}
          </List>
        </DialogContent>
      </Dialog>*/}
      
    </div>
  );
}

const Recipe = ({ setSelectedFunctions, selectedFunctions, handleSubmit,userInput }) =>{
  return(
    <div style={styles.recipe}>
      <Typography variant='h6' sx={{border: '1px solid black', padding: '8px', backgroundColor: '#f5f5f5'}}>Recipe</Typography>
      <div style={{ height: '85%'}}>
        {selectedFunctions && <Typography>{selectedFunctions.name}</Typography>}
      </div>
      <div style={styles.btnContainer}>
        <Typography>Step</Typography>

        <Button sx=
        {{color: 'white',
          backgroundColor:'#47bf5b',
          height: '80%',
          width: '50%',
          fontSize: '2rem' }}
          onClick={handleSubmit}
          >Bake!</Button>

        <Typography>AutoBake</Typography>
      </div>
    </div>
  );
}

const Input = ({userInput, setUserInput, handleChange2}) => {
  return(
    <div style={styles.inputSection}>
      <Typography variant='h6' sx={{border: '1px solid black', padding: '8px', backgroundColor: '#f5f5f5'}}>Input</Typography>
      <TextField sx={{ height: '100%', width: '100%'}} multiline rows={12}
        onChange={(e,v) => handleChange2(e,v)}
        value={userInput}></TextField>
    </div>
  );

}

const Output = ({output}) => {
  return(
    <div style={styles.inputSection}>
      <Typography variant='h6' sx={{border: '1px solid black', padding: '8px', backgroundColor: '#f5f5f5'}}>Output</Typography>
      <TextField disabled sx={{ height: '100%', width: '100%'}}
        multiline rows={12}
        value={output}></TextField>
    </div>
  );

}


const styles = {
  main: {
    width: '100vw',
    height: '93vh',
    boxSizing: 'border-box',
    padding: 0,
    margin: 0,
    display: 'flex'
  },
  topbar: {
    width: '100vw',
    height: '5vh',
    margin: 0,
    display: 'flex',
    justifyContent: 'space-between',
  },
  functions: {
    width:'20%',
    height: '100%',
    backgroundColor: '#f5f5f5',
  },
  recipe: {
    width: '30%',
    height:'100%',
    borderRight: '1px solid #f5f5f5',
    borderLeft: '1px solid #f5f5f5',
    borderBottom: '1px solid #f5f5f5',
  },
  input: {
    width: '50%',
    height: '50%',
  },
  inputSection: {
    width: '100%',
    height: '100%',
  },
  btnContainer: {
    display: 'flex',
    justifyContent: 'space-between',
    backgroundColor: '#f5f5f5',
    height: '10%',
    alignItems: 'center'
  }
}

export default App;
