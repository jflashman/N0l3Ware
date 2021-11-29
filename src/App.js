import { useState, useEffect } from 'react';
import { Container, Grid, Typography, TextField, Button, Link, List, ListItemButton} from '@mui/material';
import hash from 'js-crypto-hash';
function App() {

  const [selectedFunctions, setSelectedFunctions] = useState("");
  const [userInput, setUserInput] = useState("");
  const [output, setOutput] = useState();
  const [apiData, setApiData] = useState({});
  const [url, setUrl] = useState("http://localhost:5000/");


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
    fetch(url+ 'md2?input=' + userInput).then(
     response => response.json()
   )
   .then(
     data => {
       console.log(data)
       setOutput(data.result)
     }
   )
  }

  const handleChange = (e, value) =>{
    console.log(e, value);
    setSelectedFunctions(selectedFunctions === value ? null : value)
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
      }
        `}</style>
        <TopBar />
        <div style={styles.main}>
          <FunctionSelect {...{ selectedFunctions, setSelectedFunctions, handleChange }} />
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
        <Typography variant='h4'>Nol3Ware </Typography>
      </Grid>
      <Grid >
        <Link href='#' variant='h5' marginRight='1rem' >About/Support</Link>
        <Link href='#' variant='h5' marginRight='1rem'>Options</Link>
      </Grid>
      
    </div>

  );

}

const FunctionSelect = ({ setSelectedFunctions, selectedFunctions, handleChange }) =>{

  return (
    <div style={styles.functions}>
      <Typography variant='h6' sx={{border: '1px solid black', padding: '8px'}}>Operations</Typography>
      <List>
          <ListItemButton onClick={(e, value) => handleChange(e, "MD2 Hashing")}>
            <Typography color='blue'>MD2 Hashing</Typography>
          </ListItemButton>
          <ListItemButton  onClick={(e) =>  handleChange(e,"Translations")}>
            <Typography color='blue'>Translations +</Typography>
          </ListItemButton>
          <ListItemButton  onClick={(e) =>  handleChange(e,"Image Conversion")}>
            <Typography color='blue'>Image Conversion</Typography>
          </ListItemButton>
          <ListItemButton onClick={(e) =>  handleChange(e,"Encryption")}>
            <Typography color='blue'>Encryption +</Typography>
          </ListItemButton>
      </List>
    </div>
  );
}

const Recipe = ({ setSelectedFunctions, selectedFunctions, handleSubmit,userInput }) =>{
  return(
    <div style={styles.recipe}>
      <Typography variant='h6' sx={{border: '1px solid black', padding: '8px', backgroundColor: '#f5f5f5'}}>Recipe</Typography>
      <div style={{ height: '85%'}}>
        {selectedFunctions && <Typography>{selectedFunctions}</Typography>}
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
