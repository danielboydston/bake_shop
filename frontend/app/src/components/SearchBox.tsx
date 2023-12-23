import { createSignal, Show , createResource, For, Setter } from 'solid-js'
import {
  OutlinedInput,
  InputAdornment,
  IconButton,
  Box
} from '@suid/material'
import SearchIcon from '@suid/icons-material/Search';

type SearchBoxProps = {
  placeHolder: string | undefined
  filterSetter: Setter<string>
}

export default function SearchBox(props: SearchBoxProps) {

  return (
    <OutlinedInput sx={{mt:6}}
      fullWidth
      endAdornment={
        <InputAdornment position='end'>
          <IconButton
            aria-label='toggle password visibility'
            edge='end'
          >
            <SearchIcon/>
          </IconButton>
        </InputAdornment>
      }
      size='small'
      placeholder={props.placeHolder}
      onChange={(e) => {
        props.filterSetter(e.target.value)
      }}
    />
  )
}