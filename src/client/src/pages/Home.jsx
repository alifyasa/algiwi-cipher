import { useState } from 'react'
import {
  FormControl,
  FormLabel,
  Heading,
  Box,
  Select,
  Textarea,
  Button,
  Alert,
  AlertIcon,
  Input,
  Spinner,
  Radio,
  RadioGroup,
  Stack,
} from '@chakra-ui/react'
import { INPUT_OPTION, METHOD } from '../utils/constant';
import axios from 'axios';

export const Home = () => {
  const [inputOption, setInputOption] = useState(INPUT_OPTION.TEXT);
  const [inputText, setInputText] = useState('');
  const [inputFile, setInputFile] = useState(null);
  const [method, setMethod] = useState(METHOD.ECB);
  const [key, setKey] = useState('');
  const [encryptionLength, setEncryptionLength] = useState(1);
  const [encryptionLengthList, setEncryptionLengthList] = useState([1]);
  const [errorText, setErrorText] = useState('');
  const [result, setResult] = useState('');
  const [time, setTime] = useState(0);
  const [loading, setLoading] = useState(false);

  const getFactor = (n) => {
    let factors = [];
    for (let i = 1; i <= n; i++) {
      if (n % i === 0) {
        factors.push(i);
      }
    }
    return factors;
  }

  const encrypt = async () => {
    setErrorText('');
    setResult('');
    setLoading(true);
    let response;

    try {
      if (inputOption === INPUT_OPTION.FILE) {
        if (!inputFile) {
          setErrorText('Input file cannot be empty');
          return;
        }

        if (key === '') {
          setErrorText('Key cannot be empty');
          return;
        }

        const formData = new FormData();
        formData.append('inputOption', inputOption);
        formData.append('inputFile', inputFile);
        formData.append('method', method);
        formData.append('key', key);
        formData.append('encryptionLength', encryptionLength);

        response = await axios.post(`${import.meta.env.VITE_API_URL}/encrypt`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        if (response.data.result) {
          setResult(response.data.result);
          setTime(response.data.time);
        } else {
          setErrorText(response.data.error);
        }
      } else if (inputOption === INPUT_OPTION.TEXT) {
        if (inputText === '') {
          setErrorText('Input text cannot be empty');
          return;
        }

        
        if (key === '') {
          setErrorText('Key cannot be empty');
          return;
        }

        response = await axios.post(`${import.meta.env.VITE_API_URL}/encrypt`, {
          inputOption,
          inputText,
          method,
          key,
          encryptionLength,
        });

        if (response.data.result) {
          setResult(response.data.result);
          setTime(response.data.time);
        } else {
          setErrorText(response.data.error);
        }
      }
    } catch (e) {
      setErrorText(e.message);
    } finally {
      setLoading(false);
    }
  }

  const decrypt = async () => {
    setErrorText('');
    setResult('');
    setLoading(true);
    let response;

    try {
      if (inputOption === INPUT_OPTION.FILE) {
        if (!inputFile) {
          setErrorText('Input file cannot be empty');
          return;
        }

        if (key === '') {
          setErrorText('Key cannot be empty');
          return;
        }

        const formData = new FormData();
        formData.append('inputOption', inputOption);
        formData.append('inputFile', inputFile);
        formData.append('method', method);
        formData.append('key', key);
        formData.append('encryptionLength', encryptionLength);

        response = await axios.post(`${import.meta.env.VITE_API_URL}/decrypt`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });

        if (response.data.result) {
          setResult(response.data.result);
          setTime(response.data.time);
        } else {
          setErrorText(response.data.error);
        }
      } else if (inputOption === INPUT_OPTION.TEXT) {
        if (inputText === '') {
          setErrorText('Input text cannot be empty');
          return;
        }

        
        if (key === '') {
          setErrorText('Key cannot be empty');
          return;
        }

        response = await axios.post(`${import.meta.env.VITE_API_URL}/decrypt`, {
          inputOption,
          inputText,
          method,
          key,
          encryptionLength,
        });

        if (response.data.result) {
          setResult(response.data.result);
          setTime(response.data.time);
        } else {
          setErrorText(response.data.error);
        }
      }
    } catch (e) {
      setErrorText(e.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <>
      <Heading as="h1" size="xl" textAlign="center" my="4" mx="4">
        AlGiWi Cipher
      </Heading>
      <Box borderWidth="2px" borderRadius="md" p="4" mx="4" bg="gray.50">
        <FormControl mt="2">
          <FormLabel>Input</FormLabel>
          <Select borderWidth="1px" borderColor="black" placeholder='Select input option' defaultValue={inputOption} onChange={e => setInputOption(e.target.value)}>
            <option value={INPUT_OPTION.TEXT}>{INPUT_OPTION.TEXT}</option>
            <option value={INPUT_OPTION.FILE}>{INPUT_OPTION.FILE}</option>
          </Select>
        </FormControl>
        {inputOption === INPUT_OPTION.TEXT && <FormControl mt="2">
          <FormLabel>Text</FormLabel>
          <Textarea borderWidth="1px" borderColor="black" placeholder="Input plain text" size="sm" rows={5} value={inputText} onChange={e => setInputText(e.target.value)} />
        </FormControl>}
        {inputOption === INPUT_OPTION.FILE && <FormControl mt="2">
          <FormLabel>File</FormLabel>
          <Input type="file" borderWidth="1px" borderColor="black" size="sm" onChange={e => setInputFile(e.target.files?.length ? (e.target.files?.length > 0 ? e.target.files[0] : null) : null)} />
        </FormControl>}
        <FormControl mt="2">
          <FormLabel>Method</FormLabel>
          <Select borderWidth="1px" borderColor="black" placeholder='Select input option' defaultValue={method} onChange={e => {
              setMethod(e.target.value);
              if (e.target.value === METHOD.CFB || e.target.value === METHOD.OFB) {
                setEncryptionLength(1);
                if (key.length === 0) {
                  setEncryptionLengthList([1]);
                } else {
                  setEncryptionLengthList(getFactor(key.length * 8));
                }
              }
            }}>
            <option value={METHOD.ECB}>{METHOD.ECB}</option>
            <option value={METHOD.CBC}>{METHOD.CBC}</option>
            <option value={METHOD.OFB}>{METHOD.OFB}</option>
            <option value={METHOD.CFB}>{METHOD.CFB}</option>
            <option value={METHOD.COUNTER}>{METHOD.COUNTER}</option>
          </Select>
        </FormControl>
        <FormControl mt="2">
          <FormLabel>Key</FormLabel>
          <Textarea borderWidth="1px" borderColor="black" placeholder="Input key" size="sm" rows={1} onChange={e => {
            setKey(e.target.value)
            if (method === METHOD.CFB || method === METHOD.OFB) {
              setEncryptionLength(1);
              if (e.target.value.length === 0) {
                setEncryptionLengthList([1]);
              } else {
                setEncryptionLengthList(getFactor(e.target.value.length * 8));
              }
            }
          }} />
        </FormControl>
        {(method === METHOD.CFB || method === METHOD.OFB) && (
          <FormControl mt="2">
            <FormLabel>Encryption Length (bit)</FormLabel>
            <RadioGroup value={encryptionLength} onChange={value => setEncryptionLength(parseInt(value))}>
              <Stack direction="column">
                {encryptionLengthList.map((length, index) => (
                  <Radio key={index} value={length}>{length}</Radio>
                ))}
              </Stack>
            </RadioGroup>
          </FormControl>
        )}
        <FormControl mt="2">
          <Button colorScheme="green" size="md" mx="1" onClick={encrypt}>Encrypt</Button>
          <Button colorScheme="green" size="md" mx="1" onClick={decrypt}>Decrypt</Button>
          {errorText && (
            <Alert status="error" my="2">
              <AlertIcon />
              {errorText}
            </Alert>
          )}
        </FormControl>
        <FormControl mt="2">
          <FormLabel>Result {loading && <Spinner color="green.500" />}</FormLabel>
          <Textarea borderWidth="1px" borderColor="gray" color="gray" size="sm" rows={5} value={result} readOnly />
        </FormControl>
        <FormControl mt="2">
          <FormLabel>Time Elapsed</FormLabel>
          <Textarea borderWidth="1px" borderColor="gray" color="gray" size="sm" rows={1} value={`${time} second`} readOnly />
        </FormControl>
      </Box>
    </>
  )
}