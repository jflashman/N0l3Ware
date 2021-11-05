import { useState } from 'react';
import { Container, Grid, Typography, TextField, Button, Link, List, ListItemButton} from '@mui/material';

function App() {

  const [selectedFunctions, setSelectedFunctions] = useState(false);

  
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
          <FunctionSelect {...{ selectedFunctions, setSelectedFunctions }} />
          <Recipe  {...{ setSelectedFunctions, selectedFunctions }}/>
          <div style={styles.input}>
            <Input />
            <Output />
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

const FunctionSelect = ({ setSelectedFunctions, selectedFunctions }) =>{

  return (
    <div style={styles.functions}>
      <Typography variant='h6' sx={{border: '1px solid black', padding: '8px'}}>Operations</Typography>
      <List>
          <ListItemButton onClick={() => setSelectedFunctions(!selectedFunctions)}>
            <Typography color='blue'>MD2 Hashing</Typography>
          </ListItemButton>
      </List>
    </div>
  );
}

const Recipe = ({ setSelectedFunctions, selectedFunctions }) =>{
  return(
    <div style={styles.recipe}>
      <Typography variant='h6' sx={{border: '1px solid black', padding: '8px', backgroundColor: '#f5f5f5'}}>Recipe</Typography>
      <div style={{ height: '85%'}}>
        {selectedFunctions && <Typography>MD2 Hash</Typography>}
      </div>
      <div style={styles.btnContainer}>
        <Typography>Step</Typography>
        <Button sx={{color: 'white', backgroundColor:'#47bf5b', height: '80%', width: '50%', fontSize: '2rem' }}>Bake!</Button>
        <Typography>AutoBake</Typography>

      </div>

    </div>
    
  );
}

const Input = () => {
  return(
    <div style={styles.inputSection}>
      <Typography variant='h6' sx={{border: '1px solid black', padding: '8px', backgroundColor: '#f5f5f5'}}>Input</Typography>

    </div>
  );

}

const Output = () => {
  return(
    <div style={styles.inputSection}>
      <Typography variant='h6' sx={{border: '1px solid black', padding: '8px', backgroundColor: '#f5f5f5'}}>Output</Typography>

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
